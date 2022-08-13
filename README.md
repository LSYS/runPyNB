<div id="top"></div> 

# Run Jupyter notebooks quietly from command-line
[![PyPI](https://img.shields.io/pypi/v/runpynb?color=brightgreen&label=PyPI)](https://pypi.org/project/runpynb/)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/lsys/runpynb?label=Latest%20release)
<br>
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/runpynb?label=Python%203.6%2B)](https://pypi.org/project/runpynb/)
<br>
[![DOI](https://zenodo.org/badge/520408889.svg)](https://zenodo.org/badge/latestdoi/520408889)

`runPyNB` is a quick and dirty utility to run (and time) Jupyter notebooks from command-line and makefiles.

<!------------------- Quickstart ------------------->
## Quickstart
Install from PyPI
```bash
pip install runpynb
```

General usage: `runpynb <notebook(s)> [options]` (".ipynb" not required)

* `runpynb`: Run all notebooks in directory.

    <pre>
    $ runpynb</pre>
    ![](https://raw.githubusercontent.com/lsys/runpynb/main/assets/_docs/runall.gif)

<p align="right">(<a href="#top">back to top</a>)</p>

<!------------------------ Usage ---------------------->
## Usage

* `runpynb <notebook(s)> -q`: Run quietly (`-q`).

    <pre>
    $ runpynb hello.ipynb -q</pre>
    ![](https://raw.githubusercontent.com/lsys/runpynb/main/assets/_docs/be-quiet.gif)
    
* `runpynb <notebook(s)> -qs`: Run quietly (`-q`) as a sequence of workflow (`-s`). Errors (eg in `error.ipynb`) will break the workflow.

    <pre>
    $ runpynb error.ipynb hello.ipynb -qs</pre>
    ![](https://raw.githubusercontent.com/lsys/runpynb/main/assets/_docs/as-sequence.gif)
    
* `runpynb <notebook(s)> -o`: Save output as separate notebook (`-o`), instead of overwriting existing notebook(s).

    <pre>
    $ runpynb hello.ipynb -o</pre>
    ![](https://raw.githubusercontent.com/lsys/runpynb/main/assets/_docs/output-as-separate-notebook.gif)
    
<p align="right">(<a href="#top">back to top</a>)</p>

<!---------------------- Options ---------------------->
## Options
```bash
usage: runpynb [-h] [-t TIMEOUT] [-s] [-o] [-v VERSION] [-q] [notebooks ...]

Run (and time) Jupyter notebooks silently in command-line.

positional arguments:
  notebooks             List of Jupyter notebooks (*.ipynb) to be run
                        (default=all notebooks in path).

optional arguments:
  -h, --help            show this help message and exit
  -t TIMEOUT, --timeout TIMEOUT
                        Seconds until a cell in the notebook timesout, which
                        raises a Timeouterror exception (default is 3000=5
                        mins).
  -s, --sequence        Sequence implicit in notebook lists. If error occurs
                        somewhere, stop entire pipeline.
  -o, --output          Save output as a separate notebook with "-out"-suffix
                        (e.g. *-out.ipynb) instead of overwriting existing
                        file.
  -v VERSION, --version VERSION
                        Version of notebook to return (Default=No conversion).
                        Notebook will be converted if necessary.
  -q, --quiet           Be quiet and don't print messages (including run
                        time). Caution: Does not suppress error messages.
```
<p align="right">(<a href="#top">back to top</a>)</p>


<!----------------- Project status ----------------->
## Status
[![Documentation Status](https://readthedocs.org/projects/runpynb/badge/?version=latest)](https://runpynb.readthedocs.io/en/latest/?badge=latest)
<br>
[![Build Status](https://app.travis-ci.com/LSYS/runPyNB.svg?branch=main)](https://app.travis-ci.com/LSYS/runPyNB)
<br>
[![Tests](https://github.com/LSYS/runPyNB/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/LSYS/runPyNB/actions/workflows/tests.yml)
[![codecov](https://codecov.io/gh/LSYS/runPyNB/branch/main/graph/badge.svg?token=ZtC2IJ07Fa)](https://codecov.io/gh/LSYS/runPyNB)
<br>
[![CI](https://github.com/LSYS/runPyNB/actions/workflows/build.yml/badge.svg?branch=main)](https://github.com/LSYS/runPyNB/actions/workflows/build.yml)
<br>
[![CLI](https://github.com/LSYS/runPyNB/actions/workflows/cli.yml/badge.svg?branch=main)](https://github.com/LSYS/runPyNB/actions/workflows/cli.yml)
<br>
[![Doclinks](https://github.com/LSYS/runPyNB/actions/workflows/doclinks.yml/badge.svg?branch=main)](https://github.com/LSYS/runPyNB/actions/workflows/doclinks.yml)
<p align="right">(<a href="#top">back to top</a>)</p>
<br>


<!---------------------- About --------------------->
## More on this package

This is a lightweight package that wraps around the official Jupyter [`nbformat`](https://nbformat.readthedocs.io/en/latest/) and [`nbconvert`](https://nbconvert.readthedocs.io/en/latest/) modules.

My workflow involves using [`Jupyter notebooks`](https://jupyter.org/) to clean, and analyze data.
I use this utility to run notebooks silently from the command-line and [`Makefiles`](#usage-with-makefiles) (without converting from `.ipynb` files to `.py` files). 

Related packages are [`guoquan/runnb`](https://github.com/guoquan/runnb) and [`vinayak-mehta/nbcommands`](https://github.com/vinayak-mehta/nbcommands) with a planned enhancement `nbtime` to run Jupyter notebooks from command-line.
<p align="right">(<a href="#top">back to top</a>)</p>

<!---------------------- Build --------------------->
## Usage with Makefiles
A minimal workflow where `get-data.ipynb` takes 5000 seconds to prepare `data.csv`.
And where `analyze.ipynb` uses `data.csv` to produce `output.png`.
```makefile
.DEFAULT_GOAL := output.png

data.csv: get-data.ipynb
	runpynb $^ -t 5000
	
output.png: analyze.ipynb data.csv
	runpynb $< 
```
<p align="right">(<a href="#top">back to top</a>)</p>


<!----------------- Known issues ---------------->
## Known Issues
* [Build fails](https://github.com/LSYS/runPyNB/runs/7627883361?check_suite_focus=true) with Python 3.6 in Windows OS.
* Notebooks with long execution time will require the `timeout` option (eg `runpynb notebook.ipynb -t 10000`).

<p align="right">(<a href="#top">back to top</a>)</p>

<!-------------------- License ------------------->
## License
This package is licensed under the [MIT License](https://github.com/LSYS/runPyNB/blob/main/LICENSE).
