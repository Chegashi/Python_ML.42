import sys

str_0 = ""
sys.argv = sys.argv[1::]
for str_1 in sys.argv:
    str_0 = str_0 + ' ' + str_1
str_0 = str_0[::-1]
print(str_0.swapcase())