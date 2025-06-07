n1 = int(input("Numero 1: "))
n2 = int(input("Numero 2: "))
n3 = int(input("Numero 3: "))

if n3 > n2:
    temp = n2
    n2 = n3
    n3 = temp

if n2 > n1:
    temp = n1
    n1 = n2
    n2 = temp

if n3 > n2:
    temp = n2
    n2 = n3
    n3 = temp

print(n1)
print(n2)
print(n3)
