n = int(input('Inserisci un intero: '))

if (n < 1):
    print(1)
else:
    f = 1
    i = 1
    while i <= n:
        f *= i
        i += 1
    print(f)
