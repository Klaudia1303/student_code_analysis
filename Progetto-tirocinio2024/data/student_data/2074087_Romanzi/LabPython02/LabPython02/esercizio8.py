a=int(input('Lato a '))
b=int(input('Lato b '))
c=int(input('Lato c '))
if a>0 and b>0 and c>0 and a<b+c and b<a+c and c<b+a:
    if a==b==c:
        print('Equilatero')
    elif (a==b and b!=c and a!=c) or (b==c and b!=a and c!=a) or (c==a and c!=b and a!=b):
        print('Isoscele')
    elif a!=b!=c:
        print('Scaleno')
else:
    print('Input non valido')
