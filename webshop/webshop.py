import os
import re
from base import Task
from prompt import *
from models import gpt, gpt4
import logging
import random
from transformers import GPT2Tokenizer

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

def get_token_length(text):
    return len(tokenizer.encode(text))

max_token_length = 15000

class WebShopTask(Task):
    """
    Input (x)   : a text instruction
    Output (y)  : a text generation
    Reward (r)  : # TODO
    Input Example: 
    Output Example: 
    """
    def __init__(self):
        """
        file: a text file, each line is some sentences
        """
        super().__init__()
        self.steps = 7
        self.stops = ['\nObservation:\n', None]
        self.value_cache = {}
        self.reflections = []
    
    def test_output(self, idx: int, output: str):
        output = output.split('Action:\n')[-1]
        prompt = score_prompt + output
        score_outputs = gpt(prompt, n=5, model='gpt-4')
        scores = []
        for score_output in score_outputs:
            # print(score_output)
            pattern = r".*correctness score is (\d+).*"
            match = re.match(pattern, score_output, re.DOTALL)
            if match:
                score = int(match.groups()[0])
                scores.append(score)
            else:
                print(f'------------------score no match: {[score_output]}')
        print(scores)
        # print('------------')
        info = {'rs': scores, 'r': sum(scores) / len(scores) if scores else 0}
        return info
    
    @staticmethod
    def standard_prompt_wrap(x: str, y:str='') -> str:
        return standard_prompt.format(input=x) + y

    @staticmethod
    def generate_self_reflection(traj, question):
        
        reflect_prompt = reflection_prompt.format(trajectory=traj)
        
        reflection = gpt4(reflect_prompt)
        
        traj_with_reflection = traj + "Reflection: " + reflection[0] + "\n"
        
        reflection_mapping = {
            'question': question,
            'reflection': reflection[0]
        }

        return traj_with_reflection, reflection_mapping

    @staticmethod
    def generate_self_reflection(z, question):
        reflection_mapping = []
        trajectories = ""

        sampled_items = random.sample(z, min(3, len(z)))
        failed_trajectories = [item['trajectory'] + f"\nReward: {item['r']}\n" for item in sampled_items if isinstance(item, dict) and 'trajectory' in item and 'r' in item]
        
        for traj in failed_trajectories:
            trajectories += traj
            reflect_prompt = reflection_prompt.format(trajectory=traj)
           
            reflection = gpt(reflect_prompt)
            
            trajectories += "Reflection: " + reflection[0] + "\n"
            
            reflection_mapping.append({
                'question': question,
                'trajectory': traj,
                'reflection': reflection[0]
            })

        return reflection_mapping

    @staticmethod
    def cot_prompt_wrap(x: str, y: str = '', reflection_mapping_list=[]):
        question = x
        input = x + y
        trajectories = ""
        
        if reflection_mapping_list:
            for reflection_mapping in reflection_mapping_list:
                traj_with_reflection = reflection_mapping['trajectory'] + "Reflection: " + reflection_mapping['reflection'] + "\n"
                trajectories += traj_with_reflection
            
            prompt = prompt1_feedback.format(trajectories=trajectories, input=input)
            return prompt
        else:
            return prompt1.format(input=input)


        
    @staticmethod
    def vote_prompt_wrap(x: str, ys: list) -> str:
        prompt = score_prompt + "\n" + x + "\n\n"
        for i, y in enumerate(ys, 1):
            # y = y.replace('Plan:\n', '')
            # TODO: truncate the plan part?
            prompt += f'Choice {i}:\n{y}\n'
        return prompt
    
    @staticmethod
    def vote_outputs_unwrap(vote_outputs: list, n_candidates: int) -> list:
        vote_results = [0] * n_candidates
        for vote_output in vote_outputs:
            pattern = r".*best trajectory is .*(\d+).*"
            match = re.match(pattern, vote_output, re.DOTALL)
            if match:
                vote = int(match.groups()[0]) - 1
                if vote in range(n_candidates):
                    vote_results[vote] += 1
            else:
                print(f'vote no match: {[vote_output]}')
        return vote_results

    @staticmethod
    def compare_prompt_wrap(x: str, ys: list) -> str:
        assert len(ys) == 2, 'compare prompt only supports 2 candidates'
        
        # Extract the last Action for each trajectory
        last_actions = []
        for y in ys:
            # Split by line and reverse to start from the end
            lines = y.split('\n')[::-1]
            for line in lines:
                # Check for an Action line and get its content
                if "Action" in line:
                    last_actions.append(line.split('Action')[-1].strip(': '))
                    break

        assert len(last_actions) == 2, 'Expected to find 2 Actions'

        # Construct the prompt with the extracted Actions
        prompt = compare_prompt + f'Action 1:{last_actions[0]}\n\nAction 2:{last_actions[1]}\n'
        return prompt

    
    @staticmethod
    def compare_output_unwrap(compare_output: str):
        if 'more correct trajectory is 1' in compare_output:
            return 0
        elif 'more correct trajectory is 2' in compare_output:
            return 1
        elif "two trajectories are similarly correct" in compare_output:
            return 0.5
        else:
            print(f'-----------------compare no match: {[compare_output]}')
            return -1
    
    @staticmethod
    def value_prompt_wrap(x: str, y: str, z: list = [], reflections: list = []) -> str:
        question = x.split('\n')[0]
        if len(z) != 0:
            failed_trajectories = ""
            for traj, ref in zip(z, reflections):
                score = int(traj['r'] * 10) / 2
                trajectory = traj['trajectory']
                split_trajectory = trajectory.split('Action: ')
                first_part = split_trajectory[0]  # This part will not be modified

                # Remove the first 'Action' and corresponding 'Observation'
                remaining_parts = split_trajectory[2:]

                # Reconstruct the trajectory string
                new_trajectory = 'Action: '.join([first_part] + remaining_parts)
                traj['trajectory'] = new_trajectory
                failed_trajectories += f"{y}\n{traj}\nReflection: {ref['reflection']}\nThus the correctness score is {score}\n"
            
            inp = y + "\n\nReflection: "
            prompt = score_prompt_feedback.format(s="", trajectories=failed_trajectories, input=inp)
        else:
            inp = y + "\n\nReflection: "
            prompt = score_prompt.format(s="", input=inp)
            
        return prompt

    
    @staticmethod
    def value_outputs_unwrap(evaluate_prompt: str):
        evaluate_prompt = evaluate_prompt[0]
        if '10' in evaluate_prompt:
            return 1.0
        elif '9' in evaluate_prompt:
            return 0.9
        elif '8' in evaluate_prompt:
            return 0.8
        elif '7' in evaluate_prompt:
            return 0.7
        elif '6' in evaluate_prompt:
            return 0.6
        elif '5' in evaluate_prompt:
            return 0.5
        elif '4' in evaluate_prompt:
            return 0.4
        elif '3' in evaluate_prompt:
            return 0.3
        elif '2' in evaluate_prompt:
            return 0.2
        elif '1' in evaluate_prompt:
            return 0.1
        else:
            return -1
            
