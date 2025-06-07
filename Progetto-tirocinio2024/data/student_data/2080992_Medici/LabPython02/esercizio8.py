a=input('inserire un numero intero: ')
a=int(a)
b=input('inserire un numero intero: ')
b=int(b)
c=input('inserire un numero intero: ')
c=int(c)
if a>0 and b>0 and c>0 and a<b+c and b<a+b and c<a+b:
    print('sono lunghezze di un triangolo')
    if a!=b and b!=c and c!=a:
        print('il triangolo è scaleno')
    elif a==b or b==c or c==a:
        print('il triangolo è isoscele')
    else:
        print('il triangolo è equilatero')
else:
    print('input non valido')

    
