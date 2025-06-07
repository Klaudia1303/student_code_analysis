x=int(input("Inserisci la misura del primo lato: "))
y=int(input("Inserisci la misura del secondo lato: "))
z=int(input("Inserisci la misura del terzo lato: "))
if (x>=0 and y>=0 and z>=0)and (x<y+z and y<x+z and z<x+y):
    if x==y==z:
        print("Triangolo equilatero")
    if not (x==y or y==z or z==x):
        print("Triangolo scaleno")
    if ((x==y or y==z or z==x)and not x==y==z):
        print("Triangolo isoscele")
else:
     print("Imput non valido")