n: int = int(input('> '))
for y in range(n):
    for x in range(n):
        if x == y or n-x-1 == y or x==0 or x==n-1 or y==0 or y == n-1:
            print('*', end='')
        else:
            print(' ', end='')
    print('')