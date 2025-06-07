n1 = int(input("Inserisci un intero positivo: "))
n2 = int(input("Inserisci un intero positivo: "))

for i in range(n1, 0, -1):
    a = n1%i
    b = n2%i
    if a == 0 and b != 0:
        print(i)
