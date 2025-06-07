a=int(input("Inserisci un numero intero: "))
b=int(input("Inserisci un numero intero: "))
c=int(input("Inserisci un numero intero: "))

if((a>0 and b>0 and c>0) and (c<a+b and b<a+c and a<c+b)):
    if(a==b and b==c):
        print("Triangolo equilatero")
    elif(a==b or c==a or b==c):
        print("Triangolo isoscele")
    else:
        print("Triangolo scaleno")
else:
    print("Input non valido")

