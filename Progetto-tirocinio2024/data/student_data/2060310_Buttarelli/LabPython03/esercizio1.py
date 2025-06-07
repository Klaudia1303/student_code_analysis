n = int(input("Inserisci un numero intero maggiore di 2: "))
p = 2
if n <= 2:
    while n <= 2:
        n = int(input("Input non valido. Inserire un numero maggiore di 2: "))
    while p <= n:
        if p % 2 == 0:
            print(p, "\n")
        p += 1
else:
    while p <= n:
        if p % 2 == 0:
            print(p, "\n")
        p += 1
