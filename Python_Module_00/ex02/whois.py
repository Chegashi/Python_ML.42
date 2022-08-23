from sys import argv
import string

if (len(argv) != 2 or not argv[1].isdigit()):
    print("ERROR")
elif (int(argv[1]) == 0):
    print("I'm Zero.")
elif (int(argv[1]) % 2 == 0):
    print("I'm Even.")
else:
    print("I'm Odd.")