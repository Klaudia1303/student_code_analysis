n1=float(input("Inserisci n1: "))
n2=float(input("Inserisci n2: "))
n3=float(input("Inserisci n3: "))
if n1<n2 and n1<n3:
    if n2<n3:
        print(n3)
        print(n2)
        print(n1)
    if n3<n2:
        print(n2)
        print(n3)
        print(n1)
if n2<n1 and n2<n3:
    if n1<n3:
        print(n3)
        print(n1)
        print(n2)
    if n3<n1:
        print(n1)
        print(n3)
        print(n2)
elif n2<n1:
    print(n1)
    print(n2)
    print(n3)