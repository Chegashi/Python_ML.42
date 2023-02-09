#!/usr/bin/env python3.7

from sys import argv
import re

str = ' '.join(argv[1::])[::-1].swapcase()
str = re.sub(" +", " ", str)
if (len(str)):
    print(str)
