a=int(input("Inserisci il primo intero"))
b=int(input("Inserisci il secondo intero"))
c=int(input("Inserisci il terzo intero"))
if a>0 and b>0 and c>0 and a<b+c and b<a+c and c<a+b:
    if a==b==c:
        print("Equilatero")
    elif a==b or a==c or b==c:
        print("Isoscele")
    else:
        print("Scaleno")
else:
    print("Input non valido")
