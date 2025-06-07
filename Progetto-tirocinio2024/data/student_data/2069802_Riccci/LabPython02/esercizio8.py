a = int(input("Inserisci numero --> "))
b = int(input("Inserisci numero --> "))
c = int(input("Inserisci numero --> "))
if(a<(b+c) and b<(a+c) and c<(b+a) and a>=0 and b>=0 and c>=0):
    if(a==b and b==c):
        print("Triangolo equilatero")
    elif(a==b or a==c or b==c):
        print("Triangolo isoscele")
    else:
        print("Triangolo scaleno")
else:
    print("Input non valido")
