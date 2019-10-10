#!/usr/bin/env python

import click
from colorama import init, Fore, Style
import os
from pkg_resources import resource_filename, resource_listdir
import random


@click.command()
@click.option("-c", "--compact", is_flag=True, help="display compacted words")
@click.option("-n", "--no-color", is_flag=True, default=True, help="display uncolored words")
@click.option("-r", "--rand", type=int, help="pick random words")
@click.option("-l", "--lang", type=click.Choice(resource_listdir(__name__, "data")), default="fr", help="used language")
@click.argument("endings", type=str, nargs=-1)
def do_it(compact, no_color, rand, lang, endings):
    """A simple tool for poets."""

    init()
    colors = [Fore.RED, Fore.GREEN, Fore.BLUE, Fore.YELLOW, Fore.MAGENTA, Fore.CYAN]

    words = []

    filename = resource_filename(__name__, os.path.join("data", lang))
    with open(filename) as reader:
        for line in reader:
            word = line.strip()
            for i, ending in enumerate(endings):
                lower_ending = ending.lower()
                if word.endswith(lower_ending):
                    words.append(
                        word[: -len(lower_ending)]
                        + Style.BRIGHT
                        + colors[i % len(colors)]
                        + lower_ending
                        + Style.RESET_ALL
                        if no_color
                        else word
                    )
                    break

    if words:
        sep = "\t" if compact else "\n"
        click.echo(sep.join(random.sample(words, rand) if rand is not None and len(words) > rand else words))


if __name__ == "__main__":
    do_it()
