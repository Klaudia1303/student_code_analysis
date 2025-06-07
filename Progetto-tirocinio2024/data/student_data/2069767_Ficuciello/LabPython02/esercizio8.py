a=int(input('Inserire un primo intero:' ))
b=int(input('Inserire un secondo intero:' ))
c=int(input('Inserire un terzo intero:' ))
if a>0 and b>0 and c>0 and a<b+c and b<a+c and c<a+b:
        if a==b or a==c or b==c:
            print("isoscele")
        elif a==b==c:
            print('equilatero')
        elif a!=b!=c:
            print('scaleno')
else:
    print('input non valido')
