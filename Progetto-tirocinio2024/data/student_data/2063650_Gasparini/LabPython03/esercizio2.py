n = int(input("Numero: "))
if n <= 0:
    print("Input non valido")
else:
    i = 1
    while i <= n:
        if n % i == 0:
            print(i)
        i += 1
