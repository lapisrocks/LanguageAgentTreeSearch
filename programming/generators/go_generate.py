import re
from generators.model import ModelBase
from .generator_types import Generator
from .generator_utils import generic_generate_func_impl, generic_generate_internal_tests, generic_generate_self_reflection, generate_with_accumulated_context
from .parse import parse_code_block, add_code_block

from typing import List, Optional, Union

GO_SIMPLE_COMPLETION_INSTRUCTION = "// Write the body of this function only."
GO_REFLECTION_COMPLETION_INSTRUCTION = "You are a Go programming assistant. You will be given your past function implementation, a series of unit tests, and a hint to change the implementation appropriately. Apply the changes below by writing the body of this function only.\n\n-----"
GO_SELF_REFLECTION_COMPLETION_INSTRUCTION = "You are a Go programming assistant. You will be given a function implementation and a series of unit tests. Your goal is to write a few sentences to explain why your implementation is wrong as indicated by the tests. You will need this as a hint when you try again later. Only provide the few sentence description in your answer, not the implementation.\n\n-----"
USE_GO_CODEBLOCK_INSTRUCTION = "Use a Go code block to write your response. For example:\n```go\nfunc main() {\n    fmt.Println(\"Hello, World!\")\n}\n```"

GO_SIMPLE_CHAT_INSTRUCTION = "You are an AI that only responds with Go code, NOT ENGLISH. You will be given a function signature and its docstring by the user. Write your full implementation (restate the function signature)."
GO_REFLECTION_CHAT_INSTRUCTION = "You are an AI Go assistant. You will be given your past function implementation, a series of unit tests, and a hint to change the implementation appropriately. Write your full implementation (restate the function signature)."
GO_SELF_REFLECTION_CHAT_INSTRUCTION = "You are a Go programming assistant. You will be given a function implementation and a series of unit tests. Your goal is to write a few sentences to explain why your implementation is wrong as indicated by the tests. You will need this as a hint when you try again later. Only provide the few sentence description in your answer, not the implementation."

GO_REFLECTION_FEW_SHOT_ADD = '''Example 1:
[previous impl]:
```go
func add(a, b int) int {
    // Given integers a and b, return the total value of a and b.
	return a - b
}
```

[unit test results from previous impl]:
Tested passed:

Tests failed:
lats_test.go:49: add(1, 2) = -1, want 3
lats_test.go:49: add(2, 3) = -1, want 5

[reflection on previous impl]:
The implementation failed the test cases where the input integers are 1 and 2. The issue arises because the code does not add the two integers together, but instead subtracts the second integer from the first. To fix this issue, we should change the operator from `-` to `+` in the return statement. This will ensure that the function returns the correct output for the given input.

[improved impl]:
```Go
func add(a, b int) int {
    // Given integers a and b, return the total value of a and b.
    return a + b
}
```

END EXAMPLES
'''

GO_TEST_GENERATION_FEW_SHOT = """For example:

func signature:
/// Add three numbers together.
/// This function takes three numbers as input and returns the sum of the three numbers.
func Add3Numbers(x int, y int, z int) int {

unit tests:
func TestAdd(t *testing.T) {
    assert := assert.New(t)
    assert.Equal(7, Add3Numbers(2, 3+rand.Intn(1000)*0, 2))
    assert.Equal(15, Add3Numbers(5, 7, 3))
}
"""

GO_SELF_REFLECTION_FEW_SHOT = '''Example 1:
[function impl]:
```Go
func SortArray(array []int) []int {
// Given an array of non-negative integers, return a copy of the given array after sorting,
// you will sort the given array in ascending order if the sum( first index value, last index value) is odd,
// or sort it in descending order if the sum( first index value, last index value) is even.
// 
// Note:
// * don't change the given array.
// 
// Examples:
// * SortArray([]) => []
// * SortArray([5]) => [5]
// * SortArray([2, 4, 3, 0, 1, 5]) => [0, 1, 2, 3, 4, 5]
// * SortArray([2, 4, 3, 0, 1, 5, 6]) => [6, 5, 4, 3, 2, 1, 0]

func SortArray(array []int) []int {
	arr := make([]int, len(array))
	copy(arr, array)
	if len(arr) == 0 {
		return arr
	}
	if (arr[0]+arr[len(arr)-1])%2 == 0 {
		sort.Slice(arr, func(i, j int) bool {
			return arr[i] > arr[j]
		})
	} else {
		sort.Slice(arr, func(i, j int) bool {
			return arr[i] < arr[j]
		})
	}
	return arr
}
```

[unit test results]:
Tested passed:
func TestSortArray(t *testing.T) {
    assert := assert.New(t)
    assert.Equal([]int{}, SortArray([]int{}), \"Error\")
}
func TestSortArray(t *testing.T) {
    assert := assert.New(t)
    assert.Equal([]int{5}, SortArray([]int{5}), \"Error\")
}

Tests failed:
func TestSortArray(t *testing.T) {\n    assert := assert.New(t)\n    assert.Equal([]int{5, 4, 3, 2, 1, 0}, SortArray([]int{2, 4, 3, 0, 1, 5}), \"Error\")\n}\n # output:  []int{0, 1, 2, 3, 4, 5}, []int{5, 4, 3, 2, 1, 0}

[self-reflection]:
The implementation failed to sort the array correctly. It sorted the array in ascending order, when it needed to do it in descending order, which is not the intended behavior. The issue lies in using the sum of the first index value and the last index value as the key select if the order is ascending or descending, rather than always doing it ascending. To overcome this error, I should verify the value of the sum of the first index value and the last index value before sorting. This will ensure that the array will be sorted in the correct order, which is the desired output. Next time I approach the problem, I will make sure to use the correct sum of indexes.

END EXAMPLES

'''
GO_TEST_GENERATION_COMPLETION_INSTRUCTION = f"""You are a Go programming assistant, an AI coding assistant that can write unique, diverse, and intuitive unit tests for functions given the signature and docstring. You only responds with Go code, NOT ENGLISH.

{GO_TEST_GENERATION_FEW_SHOT}"""

GO_TEST_GENERATION_CHAT_INSTRUCTION = """You are a Go programming assistant, an AI coding assistant that can write unique, diverse, and intuitive unit tests for functions given the signature and docstring."""


def dump_tests(tests: List[str]) -> str:
    """
    Dumps the tests to a string.
    """
    return "\n".join(tests)


def parse_tests(tests: str) -> List[str]:
    """
    Parses the tests from a string.
    """
    return [test.strip() for test in tests.splitlines() if "assert" in test]

# TODO: type-check generated unit tests?


class GoGenerator(Generator):
    def self_reflection(self, func: str, feedback: str, model: ModelBase) -> str:
        return generic_generate_self_reflection(
            func=func,
            feedback=feedback,
            model=model,
            self_reflection_chat_instruction=GO_SELF_REFLECTION_CHAT_INSTRUCTION,
            self_reflection_completion_instruction=GO_SELF_REFLECTION_COMPLETION_INSTRUCTION,
            add_code_block=lambda x: add_code_block(x, "Go"),
            self_reflection_few_shot=GO_SELF_REFLECTION_FEW_SHOT,
        )
    
    def func_impl(
        self,
        func_sig: str,
        model: ModelBase,
        strategy: str,
        prev_func_impl: Optional[str] = None,
        feedback: Optional[str] = None,
        self_reflection: Optional[str] = None,
        num_comps: int = 1,
        temperature: float = 0.8,
        acc_feedback: Optional[str] = None,
        acc_reflection: Optional[str] = None,
    ) -> Union[str, List[str]]:
        if strategy == "mcts":
            return generate_with_accumulated_context(
                func_sig=func_sig,
                model=model,
                strategy="reflexion",
                prev_func_impl=prev_func_impl,
                accumulated_feedback=acc_feedback,
                accumulated_reflection=acc_reflection,
                num_comps=num_comps,
                temperature=temperature,
                reflection_chat_instruction=GO_REFLECTION_CHAT_INSTRUCTION,
                simple_chat_instruction=GO_SIMPLE_CHAT_INSTRUCTION,
                reflection_completion_instruction=GO_REFLECTION_COMPLETION_INSTRUCTION,
                simple_completion_instruction=GO_SIMPLE_COMPLETION_INSTRUCTION,
                code_block_instruction = USE_GO_CODEBLOCK_INSTRUCTION,
                reflection_few_shot=GO_REFLECTION_FEW_SHOT_ADD,
                parse_code_block=lambda x: parse_code_block(x, "go"),
                add_code_block=lambda x: add_code_block(x, "go")
            )
        else:
            return generic_generate_func_impl(
                func_sig=func_sig,
                model=model,
                strategy=strategy,
                prev_func_impl=prev_func_impl,
                feedback=feedback,
                self_reflection=self_reflection,
                num_comps=num_comps,
                temperature=temperature,
                reflection_chat_instruction=GO_REFLECTION_CHAT_INSTRUCTION,
                simple_chat_instruction=GO_SIMPLE_CHAT_INSTRUCTION,
                reflection_completion_instruction=GO_REFLECTION_COMPLETION_INSTRUCTION,
                simple_completion_instruction=GO_SIMPLE_COMPLETION_INSTRUCTION,
                code_block_instruction = USE_GO_CODEBLOCK_INSTRUCTION,
                reflection_few_shot=GO_REFLECTION_FEW_SHOT_ADD,
                parse_code_block=lambda x: parse_code_block(x, "go"),
                add_code_block=lambda x: add_code_block(x, "go"),
            )
        
    def internal_tests(
            self,
            func_sig: str,
            model: ModelBase,
            max_num_tests: int = 5
    ) -> List[str]:
        def parse_tests(tests: str) -> List[str]:
            pattern = r"(func Test\w+\(t \*testing\.T\) \{\n.+\n\})"
            matches = re.findall(pattern, tests, re.DOTALL)
            return matches
        def is_syntax_valid(test: str) -> bool:
            return True # TODO: implement this
        """
        Generates tests for a function.
        """
        return generic_generate_internal_tests(
            func_sig=func_sig,
            model=model,
            max_num_tests=max_num_tests,
            test_generation_few_shot=GO_TEST_GENERATION_FEW_SHOT,
            test_generation_chat_instruction=GO_TEST_GENERATION_CHAT_INSTRUCTION,
            test_generation_completion_instruction=GO_TEST_GENERATION_COMPLETION_INSTRUCTION,
            parse_tests=parse_tests,
            is_syntax_valid=is_syntax_valid
        )
