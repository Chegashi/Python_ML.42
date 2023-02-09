#!/usr/bin/env python3.7

phrase = "The right format"
print('{}{}'.format('-' * (42 - len(phrase)), phrase), end='')
