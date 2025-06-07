n = int(input('n: '))
unit = input('unit (C or F): ')

if unit == 'F':
    n = (n - 32)/1.8

if n <= 0:
    print('solida')
elif n >= 100:
    print('gassosa')
else:
    print('liquida')

