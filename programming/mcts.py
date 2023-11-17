from utils import enumerate_resume, make_printv, write_jsonl, resume_success_count
from executors import executor_factory
from generators import generator_factory, model_factory
from typing import List, Dict, Any
import math
from typing import Tuple
import sys

sys.set_int_max_str_digits(100000)  # Increase the limit to 10000 digits

react_prompt_header = "Here are some previous solutions and the corresponding test results.\n"
react_prompt_starter = "\n\nYour solution:\n"

class Node:
    def __init__(self, solution: str, parent=None, context="", depth=0):
        self.solution = solution
        self.parent = parent
        self.children = []
        self.value = 0
        self.visits = 0
        self.context = ""
        self.depth = depth
        self.reflection = ""
        self.test_feedback = ""

    def uct(self, exploration_weight=1.0):
        if self.visits == 0:
            #return float('inf')
            return self.value
        return (self.value / self.visits) + exploration_weight * math.sqrt(math.log(self.parent.visits) / self.visits)

    def best_child(self):
        if not self.children:  # Check if children list is empty
            return None
        return max(self.children, key=lambda child: child.uct())

    def best_child_value(self):
        if not self.children:  # Check if children list is empty
            return None
        return max(self.children, key=lambda child: child.value)

    def update(self, reward: float):
        self.visits += 1
        self.value += reward
    

def prune_context_blocks(context: str, max_length: int) -> str:
    """Prune the context to fit within the specified max_length by removing entire blocks of content using 'trial' as a delimiter."""
    if len(context) <= max_length:
        return context
    
    # Split by the block delimiter "trial".
    blocks = context.split('Previous Trial')
    
    # Remove the earliest blocks until the context fits within max_length.
    while len('trial'.join(blocks)) > max_length and blocks:
        blocks.pop(0)
    
    return 'trial'.join(blocks)

def gather_context_from_tree(node: Node) -> Tuple[List[str], List[str]]:
    """
    Given a node, walk up its tree and gather the feedback and reflections 
    from each parent node until the root is reached.

    Args:
        node (Node): The node to start gathering context from.

    Returns:
        Tuple[List[str], List[str]]: Two lists containing the accumulated feedback and reflections.
    """
    accumulated_feedback = []
    accumulated_reflection = []

    while node:
        if node.test_feedback:
            accumulated_feedback.append(node.test_feedback)
        if node.reflection:
            accumulated_reflection.append(node.reflection)
        node = node.parent

    # Reverse the lists so that the context from the earliest nodes is first
    return accumulated_feedback[::-1], accumulated_reflection[::-1]


def run_mcts(
    dataset: List[dict],
    model_name: str,
    language: str,
    max_iters: int,
    pass_at_k: int,
    log_path: str,
    verbose: bool,
    is_leetcode: bool = False,
    n: int = 5
) -> None:
    exe = executor_factory(language, is_leet=is_leetcode)
    gen = generator_factory(language)
    model = model_factory(model_name)
    test_model = model_factory("gpt4")
    print_v = make_printv(verbose)

    num_items = len(dataset)
    num_success = 0  # Counter for successful solutions
    cur_func_impl = None

    for idx, item in enumerate(dataset):
        
        cur_func_impl = None

        if is_leetcode:
            tests_i = item['visible_tests']
        else:
            tests_i = gen.internal_tests(item["prompt"], test_model, 6)

        while cur_func_impl is None:
            cur_func_impl = gen.func_impl(item["prompt"], model, "simple")
        root = Node(cur_func_impl) # initial solution (for pass@1 metric)
        
        # Lists for logging
        reflections = []
        implementations = []
        test_feedback = []
        is_solved = False

        # first attempt
        
        implementations.append(cur_func_impl)
        assert isinstance(cur_func_impl, str)
        is_passing, feedback, _ = exe.execute(cur_func_impl, tests_i)
        test_feedback.append(feedback)

        # if solved, exit early
        if is_passing:
            is_passing = exe.evaluate(
                item["entry_point"], cur_func_impl, item["test"], timeout=10)
            is_solved = is_passing
            num_success += 1
            item["acc"] = round(num_success/(idx+1), 2)
            write_jsonl(log_path, [item], append=True)
            print(num_success)
            print_v(f'completed {idx+1}/{num_items}: acc = {round(num_success/(idx+1), 2)}')
            continue
        
        reflection = gen.self_reflection(cur_func_impl, feedback, model)
        reflections += [reflection]
        root.test_feedback = feedback
        root.reflection = reflection
        
        for cur_iter in range(max_iters):
            # Selection

            node = root
            trajectory = {
                'solutions': [],
                'feedbacks': []
            }

            while node.children:
                node = node.best_child()
                trajectory['solutions'].append(node.solution)
            
            # Expansion
            for _ in range(n):
                new_solution = None
                strategy = "mcts"
                prev_func_impl = node.solution
                feedback = node.test_feedback
                reflection = node.reflection
                acc_feedback, acc_reflection = gather_context_from_tree(node)
                
                while new_solution is None:
                    new_solution = gen.func_impl(
                        func_sig=item["prompt"],
                        model=model,
                        strategy=strategy,
                        prev_func_impl=prev_func_impl,
                        feedback=feedback,
                        self_reflection=reflection,
                        acc_feedback = acc_feedback,
                        acc_reflection = acc_reflection
                    )

                combined_context = "\nPrevious Trial\n\n" + new_solution

                child = Node(new_solution, parent=node, context=combined_context, depth=node.depth + 1)
                node.children.append(child)

                # Simulation
                reward_real = 0
                for child in node.children:
                    is_passing_internal, feedback_internal, _ = exe.execute(child.solution, tests_i)
                    if not is_passing_internal:
                        reflection = gen.self_reflection(child.solution, feedback_internal, model)
                        reflections.append(reflection)
                        child.reflection = reflection
                        child.test_feedback = feedback_internal
                        child.context += "\n\nPrevious Trial\n\n" + child.solution + "\n\nTest results: \n" + feedback_internal + "\n\nSelf-reflection: " + reflection
                    else:
                        child.context += "\n\nPrevious Trial\n\n" + child.solution + "\n\nTest results: \n" + feedback_internal
                        child.reflection = ""
                        child.test_feedback = feedback_internal

                    if "Tested passed:" in feedback_internal:
                        # Split at "Tests failed:" and get the part before it (which contains the passed tests)
                        passed_section = feedback_internal.split("Tests failed:")[0]
                        # Split at "Tested passed:" and get the part after it, then count the non-empty lines
                        reward_internal = len([line for line in passed_section.split("Tested passed:")[1].splitlines() if line.strip() != ''])
                        reward_internal = reward_internal / len(tests_i)
                    else:
                        reward_internal = 0
                    if is_passing_internal or cur_iter == max_iters - 1:
                        is_passing = exe.evaluate(item["entry_point"], child.solution, item["test"], timeout=10)
                        if is_passing:
                            item["solution"] = child.solution
                            is_solved = True
                            reward_real = 1
                        break

                if is_solved:
                    break
                
                print(reward_internal)
                print(reward_real)
                reward = reward_internal + reward_real
                child.update(reward)

                # Backpropagation
                temp = child
                while temp.parent:
                    temp = temp.parent
                    temp.update(reward)
        
        # Choose the best solution after all iterations
        if is_solved:
            best_solution = item["solution"]
        else:
            best_solution = root.best_child_value().solution
            item["solution"] = best_solution

        is_passing, cur_feedback, _ = exe.execute(new_solution, tests_i)
        test_feedback.append(cur_feedback)
        is_passing = exe.evaluate(item["entry_point"], best_solution, item["test"], timeout=10)
        if is_passing:
            num_success += 1

        reflections.append("MCTS reflections")
        implementations.append(best_solution)

        item["is_solved"] = is_passing
        item["reflections"] = reflections
        item["implementations"] = implementations
        item["test_feedback"] = test_feedback
        item["acc"] = round(num_success/(idx+1), 2)
        write_jsonl(log_path, [item], append=True)
        
        print_v(f'completed {idx+1}/{num_items}: acc = {round(num_success/(idx+1), 2)}')
