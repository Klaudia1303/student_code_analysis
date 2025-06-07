a=int(input('Inserire un numero intero:'))
b=int(input('Inserire un numero intero:'))
c=int(input('Inserire un numero intero:'))
if c<b+a and a<b+c and b<a+c and a>0 and b>0 and c>0:
    if a==b and b!=c or b==c and c!=a or a==c and b!=a:
        print('Il triangolo è isoscele')
    elif a!=b and a!=c and b!=c:
        print('Il triangolo è scaleno')
    elif a==b and a==c and b==c:
        print('Il triangolo è equilatero')
else:print('input non valido')
