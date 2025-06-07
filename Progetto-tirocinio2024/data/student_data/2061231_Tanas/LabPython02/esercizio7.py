n1 = int(input("n1: "))
n2 = int(input("n2: "))
n3 = int(input("n3: "))
while not n1 > n2 > n3:
    if n3 > n2:
        n2, n3 = n3, n2
    if n2 > n1:
        n1, n2 = n2, n1
print(n1, n2, n3)
