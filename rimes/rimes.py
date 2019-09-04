#!/usr/bin/env python

import argparse
from pkg_resources import resource_filename, resource_listdir
import pprint
import random
import os


def arg_parser():
    parser = argparse.ArgumentParser(description="A simple tool for poets")
    parser.add_argument(
        "ending", metavar="ENDING", type=str, nargs="+", help="end of the word"
    )
    parser.add_argument(
        "-c", "--compact", action="store_true", help="display compacted words"
    )
    parser.add_argument(
        "-l",
        "--lang",
        type=str,
        choices=resource_listdir(__name__, "data"),
        default="fr",
        help="used language",
    )
    parser.add_argument("-r", "--rand", type=int, help="pick random words")

    return parser


def runner():
    words = []
    parser = arg_parser()
    args = parser.parse_args()
    filename = resource_filename(__name__, os.path.join("data", args.lang))
    with open(filename) as reader:
        for line in reader:
            word = line.strip()
            for arg in args.ending:
                ending = arg.lower()
                if word.endswith(ending):
                    words.append(word)
                    break

    if words:
        columns, _ = os.get_terminal_size()
        pp = pprint.PrettyPrinter(width=columns, compact=args.compact)
        pp.pprint(
            random.sample(words, args.rand)
            if args.rand is not None and len(words) > args.rand
            else words
        )


if __name__ == "__main__":
    runner()
