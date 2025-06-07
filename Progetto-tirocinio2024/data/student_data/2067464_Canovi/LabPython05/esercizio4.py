n1 = int(input("inserisci un numero naturale positivo: "))
n2 = int(input("inserisci un numero naturale positivo: "))
for i in range(1, (n2//n1) + 1):
    if n1*i != n2:
        print(n1*i)


