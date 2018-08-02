#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    name='pymath2',
    version='0.1.0',
    packages=find_packages(exclude=('tests',)),
    scripts=['scripts/pymath'],
    description='Script that launches python repl with a bunch of handy function imported',
    url='https://github.com/cjbassi/pymath',
)
