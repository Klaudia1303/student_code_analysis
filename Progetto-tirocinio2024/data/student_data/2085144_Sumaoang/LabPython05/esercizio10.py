n = int(input('Inserire la dimensione del rettangolo (un numero >= 3): '))

for x in range(n):
    for y in range(n):
        if x == 0 or x == n-1 or y == 0 or y == n-1 or y == x or y == n-1-x:
            print('*', end='')
        else:
            print(' ', end='')

    print()
