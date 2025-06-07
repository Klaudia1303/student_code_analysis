c = 0
finito = False
while not finito:
    n = input('Inserisci un intero (* per terminare): ')
    if (n == '*'):
        finito = True
    elif (int(n) <= 0):
        c += int(n)
print(c)
