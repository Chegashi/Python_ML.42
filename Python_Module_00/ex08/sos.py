from ast import arg
from sys import argv

sos = { 'a': '.-',
		'b': '-...',
		'c': '-.-.',
		'd': '-..',
		'e': '.',
		'f': '..-.',
		'g': '--.',
		'h': '....',
		'i': '..',
		'j': '.---',
		'k': '-.-',
		'l': '.-..',
		'm': '--',
		'n': '-.',
		'o': '---',
		'p': '.--.',
		'q': '--.-',
		'r': '.-.',
		's': '...',
		't': '-',
		'u': '..-',
		'v': '...-',
		'w': '.--',
		'x': '-..-',
		'y': '-.--',
		'z': '--..',
		'0': '-----',
		'1': '.----',
		'2': '..---',
		'3': '...--',
		'4': '....-',
		'5': '.....',
		'6': '-....',
		'7': '--...',
		'8': '---..',
		'9': '----.',
		' ': '/'
	}

if len(argv) == 1:
	quit()

morse = ''
for word in argv[1::]:
	for char in word:
		if (not char.isalpha() and not char.isdigit() and char != ' '):
			print('ERROR')
			quit()
		else:
			morse += " " + sos[char.lower()]
	if word != argv[-1]:
		morse += " " + sos[' '] + " "
print(morse)
