n1=int(input("Inserisci n1: "))
n2=int(input("Inserisci n2: "))
n3=int(input("Inserisci n3: "))
if (n1<0 and n2<0 and n3<0) or (n1>(n2+n3)or n2>(n1+n3)or (n3>n2+n1)):
    print("Triangolo impossibile")
elif n1==n2==n3:
    print("Triangolo equilatero")
elif not n1==n2 and not n2==n3 and not n3==n1:
    print("Triangolo scaleno")
elif ((n1==n2 or n2==n3 or n3==n1) and not n1==n2==n3):
    print("Triangolo isoscele")