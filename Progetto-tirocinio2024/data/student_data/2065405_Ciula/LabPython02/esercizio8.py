a=int(input("Inserisci un intero "))
b=int(input("Inserisci un intero "))
c=int(input("Inserisci un intero "))
if(((a>0)and(b>0)and(c>0))&((a<(b+c))and(b<(a+c))and(c<(b+a)))):
    if((a==b)and(b==c)):
        print("Triangolo equilatero")
    elif((a!=b)and(a!=c)and(c!=b)):
        print("Triangolo scaleno")
    elif((a==b)and(b!=c)):
        print("Triangolo isoscele")
    elif((a==c)and(c!=b)):
        print("Triangolo isoscele")
    elif((b==c)and(c!=a)):
        print("Triangolo isoscele")
else:
    print("Input non valido")

