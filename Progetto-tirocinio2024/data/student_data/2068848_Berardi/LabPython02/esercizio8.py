a = int(input("inserisci il lato a: "))
b = int(input("inserisci il lato b: "))
c = int(input("inserisci il lato c: "))
if a>0 and b>0 and c>0:
    if a<b+c and b<a+c and c<a+b:
        if a == b and b == c:
            print("equilatero")
        else:
            if a==b or b==c or a==c:
                print("isoscele")
            else:
                print("scaleno")
    else:
        print("input non valido")
else:
    print("input non valido") 