from sys import argv

if len(argv) != 3:
    print('InputError: too many arguments')
elif not isinstance(argv[1], int) or not isinstance(argv[2], int) :
    print('InputError: only numbers')
else:
    print('Sum:\t\t', int(argv[1]) + int(argv[2]))
    print('Difference:\t', int(argv[1]) - int(argv[2]))
    print('Product:\t', int(argv[1]) * int(argv[2]))
    if int(argv[2]) == 0:
        print('Quotient:    ERROR (div by zero')
        print('Remainder:   ERROR (modulo by zero)')

    else:
        print('Quotient:\t', int(argv[1]) / int(argv[2]))
        print('Remainder:\t', int(argv[1]) % int(argv[2]))