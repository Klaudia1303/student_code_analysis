finito = False
while (not finito):
    n = int(input('Inserisci un numero intero: '))
    if (n % 5 != 0):
        print(n)
    else:
        print(n / 5)
        finito = True
