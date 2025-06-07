a=int(input('inserisci numero a: '))
b=int(input('inserisci numero b: '))
c=int(input('inserisci numero c: '))

if a>0 and b>0 and c>0 and a<b+c and b<a+c and c<a+b:
    if a!=b and b!=c and a!=c:
        print("scaleno")
    else:
        if a==b and a!=c and b!=c or b==c and b!=a and a!=c or c==a and b!=a and b!=c:
            print("isoscele")
        else:
            print("equilatero")
else:
    print("input non valido")
    
    
    
    
