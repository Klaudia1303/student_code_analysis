n = int(input('Inserisci un numero positivo maggiore di 1: '))

i = 2
while (i <= n):
    primo = True
    k = 2
    while (k < i):
        if (i % k == 0):
            primo = False
        k += 1
    if (primo and i != 1):
        print(i)
    i += 1
