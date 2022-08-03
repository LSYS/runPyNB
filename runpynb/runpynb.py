from typing import Sequence
import os
import sys
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from nbconvert.preprocessors.execute import CellExecutionError
import asyncio

if sys.version_info[0] == 3 and sys.version_info[1] >= 8 and sys.platform.startswith("win"):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


def run_notebooks(
    notebooks: Sequence[str],
    timeout: int = 3000,
    ver: int = None,
    assequence: bool = False,
    output: bool = False,
    quiet: bool = False,
) -> None:
    """
    Takes a list of Jupyter notebooks and execute one by one.
    Parameters
    ----------
    notebooks (list-like)
            List of notebooks to be executed. ".ipynb" extension is implied and not required.
    timeout (int)
            Threshold in seconds before cell execution timeouts and throws a cell timeout error.
            (Default = 3000 -> 5 mins)
    ver (int)
            Version of notebook to convert to and return.
            (Default is None)
    assequence (bool)
            If True, order of notebooks imply workflow and and error in any one notebook will stop
            entire pipeline.
            (Default = False. If a notebook fails, move on to executing the next notebook.)
    output (bool)
            If True, save the output in a separate notebook with a "-out.ipynb" suffix. For example,
            "notebook1.ipynb" will be saved as "notebook1-output.ipynb". Otherwise the notebook will
            be overwritten.
            (Default = False)
    quiet (bool)
            If True, be quiet and suppress printing of messages.
            Default = False)
    Returns
    -------
    None
    """
    size_work = len(notebooks)
    seq_err_msg = "Error in sequence of notebooks, halting entire pipeline..."

    for ix, filename in enumerate(notebooks):
        if not os.path.isfile(filename):
            filename = "".join([filename, ".ipynb"])
        with open(filename) as f:
            if ver:
                nb = nbformat.read(f, as_version=ver)
            else:
                nb = nbformat.read(f, nbformat.NO_CONVERT)

            ep = ExecutePreprocessor(timeout=timeout, kernel_name="python3")
            print_or_quiet(f"Running notebook {ix+1}/{size_work}: {filename}", quiet=quiet)

            try:
                ep.preprocess(nb)
                print_or_quiet(f"Done {filename}.\n", quiet=quiet)
            except CellExecutionError:
                print(f"Error executing {ix+1}/{size_work}: {filename}.\n")
                if assequence:
                    sys.exit(seq_err_msg)
            except TimeoutError:
                print(f"Cell timeout error with {filename}.\n")
                if assequence:
                    sys.exit(seq_err_msg)
            finally:
                if output:
                    filename = filename.split(".")[0]
                    filename = "".join([filename, "-out.ipynb"])

                    with open(filename, mode="wt") as f:
                        nbformat.write(nb, f)
    return None


def print_or_quiet(string: str, quiet: bool = False) -> None:
    """
    If quiet = True, do not print.
    """
    if not quiet:
        print(string)
    return None
