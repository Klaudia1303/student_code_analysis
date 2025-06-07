n = int(input("Inserisci un numero: "))
f = int(input("Inserisci un numero: "))
prodotto = 0
if f < 0:
    for i in range(n):
        prodotto += f
if f > 0:
    for i in range(f):
        prodotto += n
print(prodotto)
