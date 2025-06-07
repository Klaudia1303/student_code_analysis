a=int(input())
b=int(input())
c=int(input())
if a<0 or b<0 or c<0:
    print("input non valido")
if a>0 and b>0 and c>0:
    print("triangolo")
if a>0 and b>0 and c>0:
    if a==b==c:
        print("equilatero")
    elif a!=b!=c!=a:
        print ("scaleno")
    elif a==b:
        print("isoscele")
    elif a==c:
        print("isoscele")
    elif b==c:
        print("isoscele")
