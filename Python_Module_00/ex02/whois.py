#!/usr/bin/env python3.7

from sys import argv

if (len(argv) == 1):
    exit(1)
elif (len(argv) > 2):
    print('AssertionError: more than one argument are provided')
    exit(1)
elif (not argv[1].isdigit()):
    print('AssertionError: argument is not an integer')
    exit(1)
elif (int(argv[1]) == 0):
    print("I'm Zero.")
elif (int(argv[1]) % 2 == 0):
    print("I'm Even.")
else:
    print("I'm Odd.")
