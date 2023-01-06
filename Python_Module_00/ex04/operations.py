from sys import argv

if len(argv) == 1:
    print('Usage: python operations.py <number1> <number2>')
    print('Example:\n\tpython operations.py 10 3')
elif len(argv) != 3:
    print('AssertionError: too many arguments')
elif not argv[1].isdigit() or not argv[2].isdigit():
    print('AssertionError: only integers')
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
