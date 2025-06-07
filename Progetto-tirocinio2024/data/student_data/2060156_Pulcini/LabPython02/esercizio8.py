a=int(input('intero a'))
b=int(input('intero b'))
c=int(input('intero c'))
if a+b>c and a+c>b and b+c>a and a>0 and b>0 and c>0:
    if a==b==c:
        print('equilatero')
    elif a==b!=c or a==c!=b or b==c!=a:
        print('isoscele')
    elif a!=b!=c:
        print('scaleno')
else:
    print('input non valido')
