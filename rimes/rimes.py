#!/usr/bin/env python

import argparse
from colorama import init, Fore, Style
from pkg_resources import resource_filename, resource_listdir
import random
import os


def arg_parser():
    parser = argparse.ArgumentParser(description="A simple tool for poets")

    parser.add_argument(
        "ending", metavar="ENDING", type=str, nargs="+", help="end of the word"
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


def colored(word, ending):
    return word[: -len(ending)] + Fore.BLUE + ending + Style.RESET_ALL


def runner():
    init()

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
                    words.append(colored(word, ending))
                    break

    if words:
        if args.rand is not None:
            if len(words) > args.rand:
                words = random.sample(words, args.rand)

        str = " ".join(words)
        print(str)


if __name__ == "__main__":
    runner()
