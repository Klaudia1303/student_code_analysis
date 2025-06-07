
a=int(input("Inserire primo numero:\t"))
b=int(input("Inserire secondo numero:\t"))
c=int(input("Inserire terzo numero:\t"))
if (a and b and c >0) and (c<a+b) and (b<c+a) and (a<c+b) :
    if a==b==c:
        print("Triangolo equilatero")
    elif a==b or a==c or b==c:
        print("Triangolo isoscele")
    else:
        print("Triangolo scaleno")

else:
    print("Input non valido")
