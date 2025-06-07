a=int(input("immetti lato a: "))
b=int(input("immetti lato b: "))
c=int(input("immetti lato c: "))
if a>0 and b>0 and c>0 and a<b+c and b<a+c and c<a+b:
    if a==b and a==c:
        print("equilatero")
    elif a==b or a==c:
        print("isoscele")
    else:
        print("scaleno")
else:
    print("input non valido")
