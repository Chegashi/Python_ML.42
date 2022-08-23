import sys, re

str = ' '.join(sys.argv[1::])[::-1].swapcase()
str = re.sub(" +", " ", str)
if (len(str)):
    print(str)
