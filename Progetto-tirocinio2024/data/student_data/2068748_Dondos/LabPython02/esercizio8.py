a = int(input())
b = int(input())
c = int(input())
if a>0 and b>0 and c>0 and a<(b+c) and b<(a+c) and c<(a+b):
        if a!=b!=c:
            print("scaleno")
        elif a==b==c:
            print("equilatero")
        else:
            print("isoscele")
else:
    print("input non valido")
