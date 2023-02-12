all: # Run everything
all: setup test lint clean

setup: # Setup dependencies
setup: 
	@pip install -r tests/requirements_dev.txt
	@pip install -r requirements.txt

test: # Run tests with pytest and coverage
test: 
	@rm -rf assets/notebooks/hello-out.ipynb
	coverage erase
	coverage run -m pytest
	rm assets/notebooks/hello-out.ipynb
	coverage report -m

BLACK_OPTS := -l 95
lint: # Check with mypy, pyflakes, black
lint: 
	mypy runpynb/runpynb.py --ignore-missing-imports
	python -m pyflakes runpynb/runpynb.py
	python -m pyflakes runpynb/scripts/runpynb
	python -m pyflakes tests/test_runpynb.py
	black runpynb/* $(BLACK_OPTS)
	black runpynb/scripts/runpynb $(BLACK_OPTS)
	black tests/* $(BLACK_OPTS)
	@echo "+ imports"
	isort .

rmcr: # Remove carriage return in script
rmcr:
	python ./assets/removeCR.py

clean: # Purge caches and output files
clean:	
	@rm -rf __pycache__
	@rm -rf .pytest_cache
	@rm -rf .mypy_cache
	@rm -rf .coverage
	@rm -rf assets/notebooks/hello-out.ipynb

prepack: # Prepare packaging for PyPi
prepack:
	@rm -rf dist/ runpynb.egg-info/
	@python setup.py sdist
	tar -xf dist/runpynb-0.2.*.tar.gz
	python ./assets/checkDistCR.py
	twine check dist/*

PACKAGE_FILES := build/ dist/ *.egg-info/ *.egg
cleanpack: # Remove distribution/packaging files
cleanpack:
	@rm -rf $(PACKAGE_FILES)

.DEFAULT_GOAL := help

help: # Show Help
	@egrep -h '\s#\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?# "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'
