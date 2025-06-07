a=int(input("inserisci un numero"))
b=int(input("inserisci un numero"))
c=int(input("inserisci un numero"))

if (a>0 and b>0 and c>0) and (a<b+c and b<a+c and c<b+a):
    if(a!=b!=c):
        print("scaleno")
    elif(a==b!=c):
        print("isoscele")
    elif(a==c!=b):
        print("isoscele")
    elif(c==b!=a):
        print("isoscele")
    elif(a==b and b==c and c==a):
        print("equilatero")
else:
    print("input non valido")
