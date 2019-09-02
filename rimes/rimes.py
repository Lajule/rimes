#!/usr/bin/env python

import argparse
import colorama
import pkg_resources


def arg_parser():
    parser = argparse.ArgumentParser(description="A simple tool for poets")
    parser.add_argument(
        "ending", metavar="ENDING", type=str, nargs="*", help="end of the word"
    )
    return parser


def runner():
    colorama.init()
    parser = arg_parser()
    args = vars(parser.parse_args())

    words = []
    with open(pkg_resources.resource_filename(__name__, "data/fr")) as reader:
        for line in reader:
            word = line.strip()
            for ending in args["ending"]:
                if word.endswith(ending):
                    words.append(
                        word[: -len(ending)]
                        + colorama.Fore.BLUE
                        + ending
                        + colorama.Style.RESET_ALL
                    )
                    break

    print(" ".join(words))


if __name__ == "__main__":
    runner()
