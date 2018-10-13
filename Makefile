# https://github.com/jwilm/alacritty/blob/master/Makefile

.PHONY: default
default: help

.PHONY: help
help:  ## Prints help for targets with comments
	@grep -E '^[a-zA-Z._-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: run
run:  ## Run the program locally on the command line
	PYTHONPATH=. ./scripts/pymath $(ARGS)

.PHONY: test
test: ## Run all tests
	pytest

.PHONY: build
build:  ## Build the project to prepare for uploading
	./setup.py sdist bdist_wheel --universal

.PHONY: publish
publish: build  ## Publish build to PyPI
	twine upload dist/*

.PHONY: install
install:  ## Install package locally
	pip install --user .

.PHONY: uninstall
uninstall:  ## Uninstall local package
	pip uninstall pymath2

.PHONY: clean
clean:  ## Clean all build files
	-rm -rf dist build *.egg-info
