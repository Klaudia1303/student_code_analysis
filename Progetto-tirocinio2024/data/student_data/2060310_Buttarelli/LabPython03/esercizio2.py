n = int(input("Inserisci un numero intero maggiore di 0: "))
i = 1
if n <= 2:
    while n <= 0:
        n = int(input("Input non valido. Inserire un numero maggiore di 0: "))
    print("Divisori di", n)
    while i <= n:
        if n % i == 0:
            print(i, "\n")
        i += 1
else:
    print("Divisori di", n)
    while i <= n:
        if n % i == 0:
            print(i, "\n")
        i += 1
