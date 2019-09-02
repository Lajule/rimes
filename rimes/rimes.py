#!/usr/bin/env python

import argparse
import os
import pkg_resources
import re
import unicodedata


def arg_parser():
    parser = argparse.ArgumentParser(description="A simple tool for poets")
    parser.add_argument(
        "ending", metavar="ENDING", type=str, nargs="*", help="the end of the word"
    )
    return parser


def runner():
    parser = arg_parser()
    args = vars(parser.parse_args())

    endings = [re.compile(f"{ending}$", re.IGNORECASE) for ending in args["ending"]]

    print(list(filter(lambda exp: exp.match("cacatot"), endings)))

    filename = pkg_resources.resource_filename(__name__, "data/fr")
    with open(filename) as fd:
        words = [
            word.strip()
            for word in fd.readlines()
            if len(list(filter(lambda exp: exp.match(exp, word.strip()), endings))) > 0
        ]

    print(words)


if __name__ == "__main__":
    runner()
