a=int(input("Inserire intero:"))
b=int(input("Inserire intero:"))
c=int(input("Inserire intero:"))
if a>0 and b>0 and c>0 and a<b+c and b<a+c and c<b+c:
    if a==b==c:
        print("equilatero")
    elif a==b or b==c or a==c:
        print("isoscele")
    elif a!=b!=c:
        print("scaleno")
else:
    print("input non valido")
        
