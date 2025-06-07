a = int(input("a: "))
b = int(input("b: "))

if b < 0:
    a = -a
    b = -b

prodotto = 0
for i in range(b):
    prodotto += a

print(prodotto)
