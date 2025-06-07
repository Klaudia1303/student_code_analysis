n1 = int(input("inserisci il primo numero: "))
n2 = int(input("inserisci il secondo numero: "))
n3 = int(input("inserisci il terzo numero: "))
if n1>n2>n3:
    print(n1)
    print(n2)
    print(n3)
elif n1>n3>n2:
    print(n1)
    print(n3)
    print(n2)
elif n2>n1>n3:
    print(n2)
    print(n1)
    print(n3)
elif n2>n3>n1:
    print(n2)
    print(n3)
    print(n1)
elif n3>n1>n2:
    print(n3)
    print(n1)
    print(n2)
elif n3>n2>n1:
    print(n3)
    print(n2)
    print(n1)