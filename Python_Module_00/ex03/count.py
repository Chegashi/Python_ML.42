#!/usr/bin/env python3.7

import sys


def text_analyzer(texts=""):
    """    This function counts the number of upper characters,
    lower characters, punctuation and spaces in a given text."""
    if not isinstance(texts, str):
        print("AssertionError: argument is not a string")
    else:
        if len(texts) == 0:
            print("What is the text to analyze?")
            texts = sys.stdin.readline()
        nbr_upper = 0
        nbr_lower = 0
        nbr_space = 0
        nbr_ponctuation = 0
        for c in texts:
            if c.isupper():
                nbr_upper += 1
            elif c.islower():
                nbr_lower += 1
            elif c.isspace():
                nbr_space += 1
            elif not c.isdigit():
                nbr_ponctuation += 1
        print('The text contains {} character(s):'.format(len(texts)))
        print("- {}{}".format(nbr_upper, " upper letters"))
        print("- {}{}".format(nbr_lower, " lower letters"))
        print("- {}{}".format(nbr_ponctuation, " punctuation marks"))
        print("- {}{}".format(nbr_space, " spaces"))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Error")
    else:
        text_analyzer(sys.argv[1])
