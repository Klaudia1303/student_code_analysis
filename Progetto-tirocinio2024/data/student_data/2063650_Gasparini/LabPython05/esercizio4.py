n1 = int(input("Numero 1: "))
n2 = int(input("Numero 2: "))

for i in range(n1, n2):
    if i % n1 == 0:
        print(i)
