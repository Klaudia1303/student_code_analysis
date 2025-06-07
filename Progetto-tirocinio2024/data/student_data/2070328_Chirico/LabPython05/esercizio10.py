n = int(input('lato del quadrato = '))

for i in range(n):
    for j in range(n):
        if i == j or (n-1)-j == i or i == 0 or i == n-1 or j == 0 or j == n-1:
            print('*', end='')
        else:
            print(' ', end='')
    print()
