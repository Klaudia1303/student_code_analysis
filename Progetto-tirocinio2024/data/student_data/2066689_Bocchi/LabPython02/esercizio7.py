n1 = int(input('numero intero 1: '))
n2 = int(input('numero intero 2: '))
n3 = int(input('numero intero 3: '))

if n1>n2>n3:
    print(n1, n2, n3)
elif n1>n3>n2:
    print(n1, n3, n2)
if n2>n1>n3:
    print(n2, n1, n3)
elif n2>n3>n1:
    print(n2, n3, n1)
if n3>n2>n1:
    print(n3, n2, n1)
elif n3>n1>n2:
    print(n3, n1, n2)
