n1 = int(input('Inserisci un intero positivo: '))
n2 = int(input('Inserisci un intero positivo: '))
multiplo = 0

for i in range(n1, n2):
    if i%n1 == 0:
        multiplo = i
        print(multiplo)
