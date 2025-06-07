a=int(input("a: "))
b=int(input("b: "))
c=int(input("c: "))
if a>0 and b>0 and c>0 and a<b+c and b<a+c and c<b+a:
    if a!=b and b!=c and a!=c:
        print("scaleno")
    elif a==b and b==c and a==c:
        print("equilatero")
    elif a==b or b==c or c==a:
        print("isoscele")
else:
    print("input non valido")
