a=int(input())
b=int(input())
c=int(input())
if (a>0 and b>0 and c>0):
    if (a<b+c and b<a+c and c<a+b):
        if (a==b and b==c):
            print("equilatero")
        elif (a==b or b==c or a==c):
            print("isoscele")
        else:
            print("scaleno")
    else:
        print("input non valido")
else:
    print("input non valido")
