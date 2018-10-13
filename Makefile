.PHONY: default run build upload clean install uninstall test help all interactive

default: help

help:  ## Prints help for targets with comments
	@grep -E '^[a-zA-Z._-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

run:  ## Run the program locally on the command line
	PYTHONPATH=. ./scripts/pymath $(ARGS)

test: ## Run all tests
	pytest

build:  ## Build the project to prepare for uploading
	./setup.py sdist bdist_wheel --universal

upload: build  ## Upload build to PyPI
	twine upload dist/*

install:  ## Install package locally
	pip install --user .

uninstall:  ## Uninstall local package
	pip uninstall pymath2

clean:  ## Clean all build files
	rm -rf dist build *.egg-info
