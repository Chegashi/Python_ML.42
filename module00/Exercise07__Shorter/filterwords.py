from sys import argv

if (len(argv) != 3 or not isinstance(argv[1], str)):
	print("ERROR")
for alpha in argv[1]:
	if (not alpha.isalpha() and alpha != ' '):
		argv[1] = argv[1].replace(alpha, '')
pythonest = argv[1].split()
copy = pythonest[:]
for word in copy:
	if (len(word) <= int(argv[2])):
		pythonest.remove(word)