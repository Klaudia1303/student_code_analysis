a = int(input("inserisci primo intero: "))
b = int(input("inserisci secondo intero: "))
c = int(input("inserisci terzo intero: "))
if a>0 and b>0 and c>0 and (a+b)>c and (a+c)>b and (c+b)>a:
    if a!=b and b!=c and a!=c:
        print("triangolo scaleno")
    if a==b==c:
        print("triangolo equilatero")
    if a==b and b!=c or a==c and c!=b or c==b and b!=a:
        print("triangolo isoscele")
else:
 print("input non valido")
