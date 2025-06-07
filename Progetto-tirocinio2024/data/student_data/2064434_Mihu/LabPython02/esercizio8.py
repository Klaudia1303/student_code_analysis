a=int(input("inserisci il primo lato: "))
b=int(input("inserisci il secondo lato: "))
c=int(input("inserisci il terzo lato: "))
var=bool(False)

if a<b+c and a>0:
    if b<a+c and b>0:
        if c<a+b and c>0:
            var=True
else:
    print("input non validi")

if var==True:   
    if a==b==c:
        print("triangolo equilatero")
    elif a==b!=c or a!=b==c or a==c!=b:
        print("triangolo isoscele")
    else:
        print("triangolo scaleno")
