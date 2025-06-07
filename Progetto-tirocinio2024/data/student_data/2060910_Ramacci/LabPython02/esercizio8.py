a=int(input("inserisci un numero: "))
b=int(input("inserisci un numero: "))
c=int(input("inserisci un numero: "))
if a+b<c or c+a<b or b+c<a:
    print("non si può costruire il triangolo")
elif a==b==c:
    print("triangolo equilatero")
elif a==b or b==c or a==c:
    print("triangolo isoscele")
else:
    print("triangolo scaleno")
