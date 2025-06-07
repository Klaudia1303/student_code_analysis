a=int(input('inserire un numero '))
b=int(input('inserire un numero '))
c=int(input('inserire un numero '))
if a+b<c or a+c<b or b+c<a:
    print('input invalido')
else:
    if a!=c and b!=c and a!=b:
        print('il triangolo è scaleno')
    elif a==c and c!=b:
        print('il triangolo è isoscele')
    elif b==c and a!=c:
        print('il triangolo è isoscele')
    elif a==c and b!=c:
        print('il triangolo è isoscele')
    else:
        print('il triangolo è equilatero')
