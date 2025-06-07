n = int(input('Inserisci un intero: '))

for i in range(1, n + 1, 2):
    print(' ' * ((n - i) // 2) + '*' * i + ' ' * ((n - i) // 2))
