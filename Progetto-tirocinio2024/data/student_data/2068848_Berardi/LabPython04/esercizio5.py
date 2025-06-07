n = int(input("Inserisci il numero: "))
if n == 0:
    print(1)
else:
    i = 1
    tot = 1
    while i<=n:
        tot *= i
        i += 1
    print(tot)
