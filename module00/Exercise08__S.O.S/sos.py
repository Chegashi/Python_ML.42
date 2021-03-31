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
		'9': '----.'
	}

string = ''

argv = argv[1::]
for word in argv:
	string += ' ' + word
string = string.lower()
for char in string:
	if (not char.isalpha() and not char.isdigit() and char != ' '):
		print('ERROR')
		break;
	else:
		for char in string:
			if char != ' ':
				print(sos[char], end=' ')
			else :
				print(' / ', end='')
		print()
# 	if (char == ' '):
# 		print(' / ')
	