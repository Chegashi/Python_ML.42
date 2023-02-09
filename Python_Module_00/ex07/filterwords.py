#!/usr/bin/env python3.7

from sys import argv

if (len(argv) != 3 or argv[1].isdigit() or not argv[2].isdigit()):
    print("ERROR")
    exit()

for alpha in argv[1]:
    if (not alpha.isalpha() and alpha != ' '):
        argv[1] = argv[1].replace(alpha, '')
pythonest = argv[1].split()
copy = pythonest[:]
newpythonest = [word for word in copy if len(word) > int(argv[2])]
print(newpythonest)
