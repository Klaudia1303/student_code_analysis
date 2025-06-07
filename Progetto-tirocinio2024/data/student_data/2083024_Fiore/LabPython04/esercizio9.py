n = int(input("inserisic un numero intero positivo per stampare n numeri della successione di fibonacci: "))
c = 0
n1 = 1
n2 = 1
print(n1, "\n", n2, sep= "")
while c < (n - 2):
    somma = n1 + n2
    n1 = n2
    n2 = somma
    print(somma)
    c += 1
