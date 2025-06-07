a=int(input("a"))
b=int(input("b"))
c=int(input("c"))
if a==b==c :
    print("equilatero")
elif a==b!=c :
    print("isocele")
elif a!=b!=c :
    print("scaleno")
elif a<0 or b<0 or c<0 or a>b+c or b>a+c or c>a+b :
    print("input non valido")

    
