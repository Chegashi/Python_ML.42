import sys
import string

if (len(sys.argv) != 2 or not sys.argv[1].isdigit()):
    print("ERROR")
elif (int(sys.argv[1]) == 0):
    print("I'm Zero.")
elif (int(sys.argv[1]) % 2 == 0):
    print("I'm Even.")
else:
    print("I'm Odd.")