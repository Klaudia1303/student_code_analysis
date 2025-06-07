s = int(input('Inserisci un intero maggiore o uguale a 0: '))
n = 1
if s == 0 or s == 1:
    print(1)
elif s > 1:
    while s > 1:
        n = n * s
        s -= 1
    if s == 1:
        print (n)
