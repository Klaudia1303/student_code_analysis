a=int(input('a: '))
b=int(input('b: '))
c=int(input('c: '))
if a<b+c and b<c+a and c<a+b and a>0 and b>0 and c>0:
    if a==b==c:
        print('equilatero')
    elif a==b!=c or b==c!=a or a==c!=c:
        print('isoscele')
    elif a!=b!=c:
        print('scaleno')
else:
    print('input non valido')
