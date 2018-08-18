# pymath

Perform quick calculations either on the command line or in the Python repl. Imports and provides for use all of the functions from `math`, `itertools`, and `statistics` along with some extra math functions defined in the [pymath](https://github.com/cjbassi/pymath/tree/master/pymath) folder.

## Installation

**Note**: `~/.local/bin` should be in your `PATH` for `--user` installs.

```shell
pip install [--user] pymath2
```

## Usage

Uses [python-fire](https://github.com/google/python-fire) to handle input.

### Command line

Run a function from the command line by doing:

```shell
> pymath factorial 5
120
```

or run an expression with:

```
> pymath 'factorial(5)+1'
121
```

### Repl

To start the repl, do:

```shell
> pymath -- --interactive

>>> factorial(5)
120
>>>
```
