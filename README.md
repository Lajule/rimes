# rimes

A Python command line tool to help you to find the right rhyme.

## Installation

```sh
pip install https://github.com/Lajule/rimes/archive/master.zip
```

## Usage

Type the following command `rimes -h` to display this help message:

```
usage: rimes.py [-h] [-c] [-n] [-l {fr}] [-r RAND] ENDING [ENDING ...]

A simple tool for poets

positional arguments:
  ENDING                end of the word

optional arguments:
  -h, --help            show this help message and exit
  -c, --compact         display compacted words
  -n, --no-color        display uncolored words
  -l {fr}, --lang {fr}  used language
  -r RAND, --rand RAND  pick random words
```

## Example

```sh
rimes -n -c -r 5 tot tôt
laptot  bientôt plutôt  hottentot       tôt
```
