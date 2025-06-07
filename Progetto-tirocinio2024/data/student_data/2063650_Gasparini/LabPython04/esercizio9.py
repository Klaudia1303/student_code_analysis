n = int(input("Numero: "))

a = 0
b = 1
for i in range(n):
    print(b)
    somma = a + b
    a = b
    b = somma
