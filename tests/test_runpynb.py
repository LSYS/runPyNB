from runpynb import run_notebooks
import io
from contextlib import redirect_stdout
import pytest
import os


NOTEBOOKS_DIR = "assets/notebooks"
hello_nb = os.path.join(NOTEBOOKS_DIR, "hello.ipynb")
error_nb = os.path.join(NOTEBOOKS_DIR, "error.ipynb")
timeout3_nb = os.path.join(NOTEBOOKS_DIR, "timeout3.ipynb")


def test_run_notebooks():
    with io.StringIO() as output:
        with redirect_stdout(output):
            run_notebooks(notebooks=[hello_nb])
        stdout = output.getvalue()
    assert "running notebook" in stdout.lower()
    assert "done" in stdout.lower()

    # notebook has cell that takes 5 second but timeout=1
    # should fail with "Cell timeout error with timeout3.ipynb."
    with io.StringIO() as output:
        with redirect_stdout(output):
            run_notebooks(notebooks=[timeout3_nb], timeout=1)
        stdout = output.getvalue()
    assert f"cell timeout error with {timeout3_nb}" in stdout.lower()

    # should pass with timeout set to 4
    with io.StringIO() as output:
        with redirect_stdout(output):
            run_notebooks(notebooks=[timeout3_nb], timeout=4)
        stdout = output.getvalue()
    assert f"done {timeout3_nb}" in stdout.lower()

    # notebook with error should fail
    with io.StringIO() as output:
        with redirect_stdout(output):
            run_notebooks(notebooks=[error_nb])
        stdout = output.getvalue()
    assert "error executing" in stdout.lower()
    assert f"{error_nb}" in stdout.lower()

    # test multiple notebooks
    # first should run and second should fail
    with io.StringIO() as output:
        with redirect_stdout(output):
            run_notebooks(notebooks=[hello_nb, error_nb])
        stdout = output.getvalue()
    assert "done" in stdout.lower()
    assert "error executing" in stdout.lower()

    # test multiple notebooks
    # first should run and second should fail
    with pytest.raises(SystemExit) as info:
        run_notebooks(notebooks=[hello_nb, error_nb], assequence=True)
    assert str(info.value) == "Error in sequence of notebooks, halting entire pipeline..."

    # Should get an output file
    run_notebooks(notebooks=[hello_nb], output=True)
    hello_nb_out = os.path.join(NOTEBOOKS_DIR, "hello-out.ipynb")
    assert os.path.exists(hello_nb_out)
