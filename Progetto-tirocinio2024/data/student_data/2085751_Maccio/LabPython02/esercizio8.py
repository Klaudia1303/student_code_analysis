a=int(input("Inserire un numero intero:  "))
b=int(input("Inserire un numero intero:  "))
c=int(input("Inserire un numero intero:  "))
if a>0 and b>0 and c>0 and b<a+c and a<b+c and c<a+b:
    if a==c and b==c:
        print("Triangolo Equilatero")
    elif a==c and a!=b:
        print("Triangolo Isoscele")
    elif a!=c and c!=b:
        print("Triangolo Scaleno")
else:
    print("Input non valido")
