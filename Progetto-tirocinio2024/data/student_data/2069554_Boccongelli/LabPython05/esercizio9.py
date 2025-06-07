n = int(input('Inserisci un intero: '))

for i in range(1, n + 1):
    #hehe
    print('*' + '*' * ((n // ((i % n) + (i // n) + (n - 1))) * (n - 2)) + ' ' * ((((n // ((i % n) + (i // n) + (n - 1))) -1) * -1) * (n - 2)) + '*')
