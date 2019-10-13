# rimes

A Python command line tool to help you to find the right rhyme.

## Installation

```sh
pip install https://github.com/Lajule/rimes/archive/master.zip
```

## Usage

Type the following command `rimes --help` to display this help message:

```
Usage: rimes.py [OPTIONS] [ENDINGS]...

  A simple tool for poets.

Options:
  -c, --compact       display compacted words
  -n, --no-color      display uncolored words
  -r, --rand INTEGER  pick random words
  -l, --lang [fr]     used language
  --help              Show this message and exit.
```

## Example

```sh
rimes -n -c -r 5 tot tôt
laptot  bientôt plutôt  hottentot       tôt
```

## Languages

To support other languages, simply add language file to `data` package directory, for example try:

```sh
curl -o rimes/data/en https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt
```
