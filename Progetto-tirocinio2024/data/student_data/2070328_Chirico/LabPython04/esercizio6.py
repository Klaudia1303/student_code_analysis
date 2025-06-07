#calcolare il prodotto senza usare '*' o '/'

n = int(input("intero 1 = "))
m = int(input("intero 2 = "))
x = n

if m == 0:
    print("prodotto = ",0)
else:
    while m > 1:
        x = x+n
        m = m-1

    print("prodotto = ",x)
