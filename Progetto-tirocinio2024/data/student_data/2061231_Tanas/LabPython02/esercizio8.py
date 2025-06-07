a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
if (a>0 and b>0 and c>0) and (a<b+c and b<a+c and c<a+b):
    if a==b==c:
        print("equilatero")
    elif a==b or a==c or c==b:
        print("isoscele")
    else:
        print("scaleno")
else:
    print("input non valido")
