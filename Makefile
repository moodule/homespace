.PHONY: clean clean-test clean-pyc clean-build docs help
.DEFAULT_GOAL := help
ENVIRONMENT := poetry run

help:
	@echo "init.............install the dependencies in a local environment"
	@echo "clean............remove all build, test, coverage and Python artifacts"
	@echo "clean-build......remove build artifacts"
	@echo "clean-pyc........remove Python file artifacts"
	@echo "clean-test.......remove test and coverage artifacts"
	@echo "help.............show this help message"
	@echo "lint.............check code style agains the PEP"
	@echo "test.............run tests quickly with the default Python"

init:
	poetry install

clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts

lint: ## check style with flake8
	$(ENVIRONMENT) flake8 adspying tests

test: ## run tests quickly with the default Python
	$(ENVIRONMENT) python -m unittest
