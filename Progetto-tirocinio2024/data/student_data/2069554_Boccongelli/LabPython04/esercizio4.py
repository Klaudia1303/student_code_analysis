c = 0
finito = False
while not finito:
    n = int(input('Inserisci un intero: '))
    if (n == 0):
        finito = True
    elif (n % 3 == 0):
        c += n
print(c)
