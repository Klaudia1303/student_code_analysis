a=int(input("Inserisci primo numero: "))
b=int(input("Inserisci secondo numero: "))
c=int(input("Inserisci terzo numero: "))
if a>0 and b>0 and c>0 and a<b+c and b<a+c and c<a+b:
    if a!=b and a!=c and b!=c:
        print("scaleno")
    elif a==b and a==c and b==c:
        print("equilatero")
    else:
        print("isoscele")
else: print("input non valido")
        
