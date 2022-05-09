calc = True
sign = ['+', '-', '/', 'x', '*', '^']

while calc:
    num_1 = float(input('Enter a number: '))
    op = input('Operation: ')
    num_2 = float(input('Enter another number: '))
    if op == sign[0]:
        print(f'\t{num_1 + num_2}\n') 
    elif op == sign[1]:
        print(f'\t{num_1 - num_2}\n') 
    elif op == sign[2]:
        print(f'\t{num_1 / num_2}\n') 
    elif op == sign[3] or op == sign[4]:
        print(f'\t{num_1 * num_2}\n')
    elif op == sign[5]:
        print(f'\t{num_1 ** num_2}\n') 
    else:
        print('Try Casio, e ma kpa mi.\n')
