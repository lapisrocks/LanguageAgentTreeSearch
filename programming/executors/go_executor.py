import os
import subprocess
import tempfile

from executor_types import ExecuteResult, Executor

from typing import List, Tuple, Optional
import re


def create_temp_project() -> Tuple[str, str, str]:
    # get id of the process
    pid = os.getpid()
    # get random number
    rand = os.urandom(8).hex()
    # create a temp directory
    temp_path = tempfile.gettempdir()
    temp_dir = f"{temp_path}/go-lats-{pid}-{rand}"
    # delete the temp directory if it exists
    if os.path.exists(temp_dir):
        os.system(f"rm -rf {temp_dir}")
    os.mkdir(temp_dir)
    # initialize a go project
    os.chdir(temp_dir)
    os.system(f"go mod init go-lats-{pid}-{rand}")
    main_path = os.path.join(temp_dir, "lats.go")
    test_path = os.path.join(temp_dir, "lats_test.go")
    return temp_dir, main_path, test_path


def write_to_file(path: str, code: str, package: str = "main"):
    prelude = f"package {package}\n\n"
    postlude = ""
    code = prelude + code + postlude
    # delete the file if it exists
    if os.path.exists(path):
        os.remove(path)
    # write the code to the file
    with open(path, "w") as f:
        f.write(code)


def format_files(paths: List[str]):
    for path in paths:
        os.system(f"go fmt {path}")
        os.system(f"goimports -w {path}")


def download_imports(tmp_cargo_path: str):
    os.system(f"cd {tmp_cargo_path} && go get -d ./... && go mod tidy")


def write_to_file_toplevel(path: str, code: str):
    # delete the file if it exists
    if os.path.exists(path):
        os.remove(path)
    # write the code to the file
    with open(path, "w") as f:
        f.write(f"package lats\n\n{code}")


def run_process(cmd: str, tmp_path: str, timeout: int = 5, print_debug: bool = False) -> Optional[Tuple[str, str]]:
    """
    Runs the given command. Produces a tuple of stdout and stderr.
    """
    # run the command
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE, cwd=tmp_path)
    out, err = p.communicate()

    # decode the output
    out = out.decode("utf-8")
    err = err.decode("utf-8")
    if print_debug:
        print("## RUN OUTPUTS ##")
        print("STDOUT:")
        print(out)
        print("STDERR:")
        print(err, flush=True)

    return out, err


class GoExecutor(Executor):
    def execute(self, func: str, tests: List[str], timeout: int = 5) -> ExecuteResult:
        # Combine function code and assert statement
        tmp_dir, temp_file, temp_test = create_temp_project()

        # run go get to download the dependencies
        write_to_file(temp_file, func, "lats")
        format_files([temp_file])
        download_imports(tmp_dir)

        res = run_process(
            "go build ./...", tmp_dir, timeout=timeout)
        assert res is not None, "Timeout in go get"

        errs = grab_compile_errs(res[1])  # (check returns stdin)
        if len(errs) > 0:
            # cleanup the temp directory
            os.system(f"rm -rf {tmp_dir}")
            state = tuple([False] * len(tests))

            err_str = ""
            for err in errs:
                err_str += f"\n{err}"

            return ExecuteResult(False, err_str, state)

        # Run the tests and collect the results
        tests_res: List[Tuple[bool, str]] = []
        num_tests = len(tests)
        for i in range(num_tests):
            """
            # use some sort of timeout limit to handle infinite loops
            if pass, add to success tests
            if fail, add to failed tests with the log from the compiler
            """
            write_to_file(temp_test, tests[i], "lats")
            format_files([temp_test])
            download_imports(tmp_dir)

            # run go test
            res = run_process("go test ./...", tmp_dir, timeout=timeout)
            if res is None:
                tests_res.append((False, "Timeout"))
                continue

            # check if we have any compile errors in the test
            errs = grab_compile_errs(res[1])  # (check returns stdin)
            if len(errs) > 0:
                # cleanup the temp directory
                tests_res.append((False, str(errs[1])))
                continue

            # check if we have any failed tests
            errs = grab_test_errs(res[0])
            if len(errs) > 0:
                tests_res.append((False, str(errs[0])))
                continue

            # if we get here, the test passed
            tests_res.append((True, ""))

        # cleanup the temp directory
        os.system(f"rm -rf {tmp_dir}")

        passed_str = ""
        failed_str = ""
        state = []
        for i, (passed, output) in enumerate(tests_res):
            test = tests[i]
            if passed:
                passed_str += f"\n{test}"
            else:
                failed_str += f"\n{test} // output: {output}"
            state.append(passed)

        feedback = "Tested passed:"
        feedback += passed_str
        feedback += "\n\nTests failed:"
        feedback += failed_str

        is_passing = len(failed_str) == 0

        return ExecuteResult(is_passing, feedback, tuple(state))

    def evaluate(self, name: str, func: str, test: str, timeout: int = 5) -> bool:
        """
        Evaluates the implementation on Human-Eval Rust (MultiPL-E generated,

        Federico Cassano, John Gouwar, Daniel Nguyen, Sydney Nguyen, Luna Phipps-Costin, Donald Pinckney, Ming-Ho Yee, Yangtian Zi, Carolyn Jane Anderson, Molly Q Feldman, Arjun Guha, Michael Greenberg, Abhinav Jangda ).
        If you use this function please cite:
        @misc{cassano2022multiple,
          title={MultiPL-E: A Scalable and Extensible Approach to Benchmarking Neural Code Generation}, 
          author={Federico Cassano and John Gouwar and Daniel Nguyen and Sydney Nguyen and Luna Phipps-Costin and Donald Pinckney and Ming-Ho Yee and Yangtian Zi and Carolyn Jane Anderson and Molly Q Feldman and Arjun Guha and Michael Greenberg and Abhinav Jangda},
          year={2022},
          eprint={2208.08227},
          archivePrefix={arXiv},
          primaryClass={cs.LG}
        })

        TODO: do it actually
        """
        tmp_dir, tmp_path, test_path = create_temp_project()
        print(f"Evaluating\n{func}\n\n{test}", flush=True)
        write_to_file_toplevel(tmp_path, func)
        write_to_file_toplevel(test_path, test)
        format_files([tmp_path, test_path])
        download_imports(tmp_dir)

        res = run_process(
            "go build ./...", tmp_dir, timeout=timeout, print_debug=True)
        assert res is not None, "Timeout building the project"

        errs = grab_compile_errs(res[0])  # (check returns stdin)
        if len(errs) > 0:
            # cleanup the temp directory
            os.system(f"rm -rf {tmp_dir}")
            print("Compile errors. Failed eval", flush=True)
            return False

        # compile and run the binary
        res = run_process("go test ./...", tmp_dir,
                               timeout=timeout, print_debug=True)
        os.system(f"rm -rf {tmp_dir}")

        if res is None:
            print("Timeout?. Failed eval", flush=True)
            return False
        else:
            # check if we have any compile errors in the test
            errs = grab_compile_errs(res[1])  # (check returns stdin)
            if len(errs) > 0:
                print("Compile errors. Failed eval", flush=True)
                return False
            errs = grab_test_errs(res[0])
            if len(errs) > 0:
                print("Test errors. Failed eval", flush=True)
                return False

            print("Passed eval", flush=True)
            return len(errs) == 0


assert_no_panic = r"""
macro_rules! assert_eq_nopanic {
    ($left:expr, $right:expr) => {
        std::panic::catch_unwind(|| {
            assert_eq!($left, $right);
        }).unwrap_or_else(|_| {});
    };
    () => {};
}
"""


def transform_asserts(code: str) -> str:
    """
    Transform all asserts into assert_eq_nopanic! asserts, inserting the macro
    definition at the top of the code.
    """
    code.replace("assert_eq!", "assert_eq_nopanic!")
    return assert_no_panic + code


def revert_asserts(code: str) -> str:
    """
    Revert all assert_eq_nopanic! asserts back into assert_eq! asserts.
    """
    normal = code.replace("assert_eq_nopanic!", "assert_eq!")
    # remove the macro definition
    return normal[len(assert_no_panic):]


class CompileErr:
    def __init__(self, rendered):
        self.rendered = rendered

    def __str__(self):
        return self.rendered

    def __repr__(self):
        return "{" + str(self) + "}"


class RuntimeErr:
    def __init__(self, left, right, line, column, panic_reason):
        # right and left are only used for assert_eq! errors
        self.left = left
        self.right = right
        # NOTE: currently not using the below
        self.line = line
        self.column = column
        self.panic_reason = panic_reason

    def __str__(self):
        if self.left is not None and self.right is not None:
            return f"assertion failed: {self.left} == {self.right}"
        else:
            return self.panic_reason

    def __repr__(self):
        return "{" + str(self) + "}"


# assumes that the input is the stdout of cargo check --message-format=json
# returns a list of compile errors as CompileErr objects
def grab_compile_errs(inp: str) -> List[CompileErr]:
    # we get a stream of json objects, so we need to parse them one by one
    objs = []
    compileErr = ""
    for line in inp.splitlines():
        if line == "":
            continue
        if line.startswith("#"):
            continue
        if line.startswith(".\\lats.go"):
            if compileErr != "":
                objs.append(CompileErr(compileErr))
            compileErr = line.strip() + "\n"
        if line.startswith("        "):
            compileErr += line.strip() + "\n"
    
    if compileErr != "":
        objs.append(CompileErr(compileErr))

    return objs

# assumes that the given input is the stderr of cargo run.
# returns a list of failed assertions as RuntimeErr objects


def grab_test_errs(inp: str) -> List[RuntimeErr]:
    failed_asserts = []
    for line in inp.splitlines():
        if line.startswith("        lats_test.go"):
            pattern = r"^(?:.+):(\d+): (.+)$"

            match = re.match(pattern, line.strip())
            if match:
                lineNo = match.group(1)
                panicReason = match.group(2)
            failed_asserts.append(RuntimeErr(
                None, None, lineNo, None, panicReason))

    return failed_asserts


if __name__ == "__main__":

    test_compiletime = r"""
# go-lats-35116-6739b2903daabf6d
.\lats.go:10:7: undefined: math
.\lats.go:11:18: too many return values
        have (bool, bool)
        want (bool)
.\lats.go:15:16: too many return values
        have (bool, bool)
        want (bool)
    """

    compile_errs = grab_compile_errs(test_compiletime)
    print(compile_errs)
    assert(len(compile_errs) == 3)


    test_runtime = r"""
--- FAIL: TestHasCloseElements (0.00s)
    --- FAIL: TestHasCloseElements/all_elements_equal (0.00s)
        lats_test.go:53: HasCloseElements() = false, want true
    --- FAIL: TestHasCloseElements/negative_threshold (0.00s)
        lats_test.go:53: HasCloseElements() = false, want true
FAIL
FAIL    go-lats-35116-6739b2903daabf6d  2.672s
FAIL
    """

    test_errs = grab_test_errs(test_runtime)
    print(test_errs)
    assert(len(test_errs) == 2)
