a=int(input('lato1:'))
b=int(input('lato2:'))
c=int(input('lato3:'))
if(a>0,b>0,c>0)and(a<b+c)and(b<c+a)and(c<a+b)==True:
    x=('triangolo')
    if(x=='triangolo')and(a==b==c)==True:
        print('equilatero')
    if(x=='triangolo')and(a==b!=c)or(b==c!=a)or(a==c!=b)==True:
        print('isoscele')
    if(x=='triangolo')and(a!=b!=c)==True:
        print('scaleno')
else:
    print('input non valido')
