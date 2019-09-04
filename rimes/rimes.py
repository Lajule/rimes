#!/usr/bin/env python

import argparse
import os
from pkg_resources import resource_filename, resource_listdir
import pprint
import random
import shutil


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
    parser = arg_parser()
    args = parser.parse_args()

    words = []
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
        columns, _ = shutil.get_terminal_size()
        output = pprint.pformat(
            random.sample(words, args.rand)
            if args.rand is not None and len(words) > args.rand
            else words,
            width=columns,
            compact=args.compact,
        )
        print(output)


if __name__ == "__main__":
    runner()
