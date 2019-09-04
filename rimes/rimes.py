#!/usr/bin/env python

import argparse
from colorama import init, Fore, Style
import os
from pkg_resources import resource_filename, resource_listdir
import random


def arg_parser():
    languages = resource_listdir(__name__, "data")

    parser = argparse.ArgumentParser(description="A simple tool for poets")

    parser.add_argument("ending", metavar="ENDING", type=str, nargs="+", help="end of the word")
    parser.add_argument("-c", "--compact", action="store_true", help="display compacted words")
    parser.add_argument("-n", "--no-color", action="store_false", help="display uncolored words")
    parser.add_argument("-l", "--lang", type=str, choices=languages, default="fr", help="used language")
    parser.add_argument("-r", "--rand", type=int, help="pick random words")

    return parser


def runner():
    init()
    colors = [Fore.RED, Fore.GREEN, Fore.BLUE, Fore.YELLOW, Fore.MAGENTA, Fore.CYAN]

    parser = arg_parser()
    args = parser.parse_args()

    words = []

    filename = resource_filename(__name__, os.path.join("data", args.lang))
    with open(filename) as reader:
        for line in reader:
            word = line.strip()
            for i, arg in enumerate(args.ending):
                ending = arg.lower()
                if word.endswith(ending):
                    words.append(
                        word[: -len(ending)] + Style.BRIGHT + colors[i % len(colors)] + ending + Style.RESET_ALL
                        if args.no_color
                        else word
                    )
                    break

    if words:
        sep = "\t" if args.compact else "\n"
        print(sep.join(random.sample(words, args.rand) if args.rand is not None and len(words) > args.rand else words))


if __name__ == "__main__":
    runner()
