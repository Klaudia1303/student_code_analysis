n: int = int(input('n: '))
d: int = int(input('d: '))

if n < d:
    print('propria')
elif n > d and n % d != 0:
    print('impropria')
elif n % d == 0:
    print('apparente')