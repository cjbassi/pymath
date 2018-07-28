.PHONY: default run build upload clean install uninstall

default: upload

run:
	PYTHONPATH=. ./scripts/pymath

build:
	./setup.py sdist bdist_wheel --universal

upload: build
	twine upload dist/*

install:
	pip install --user .

uninstall:
	pip uninstall pymath

clean:
	rm -rf dist build *.egg-info
