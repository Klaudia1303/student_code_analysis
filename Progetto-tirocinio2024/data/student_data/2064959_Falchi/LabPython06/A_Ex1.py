n1 = int(input("Inserire valore n1: "))
n2 = int(input("Inserire valore n2: "))

for i in range(n1, 0, -1):
    if n1 % i == 0 and n2 % i != 0:
        print(i)
