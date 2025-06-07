n1 = int(input('Inserisci un intero: '))
n2 = int(input('Inserisci un intero: '))

for i in range(n1, 0, -1):
    if (n1 % i == 0 and n2 % i != 0):
        print(i)
