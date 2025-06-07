n1 = int(input('Inserisci un intero: '))
n2 = int(input('Inserisci un intero: '))

for i in range(1, n2 // n1 + 1):
    if (i * n1 < n2):
        print(i * n1)
