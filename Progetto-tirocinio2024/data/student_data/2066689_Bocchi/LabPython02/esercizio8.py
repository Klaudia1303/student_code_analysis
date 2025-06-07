a = int(input('numero intero1: '))
b = int(input('numero intero2: '))
c = int(input('numero intero3: '))

if a>0 and b>0 and c>0:
    if a+b > c and a+c > b and b+c > a:     
        if a != b != c:
            print('scaleno')
        elif a==b and c!=a and c!=b or a==c and b!=a and b!=c or b==c and a!=b and a!=c:
            print('isoscile')
        elif a == b == c:
            print('equilatero')
    else:
        print('imput non valido')
else:
    print('imput non valido')
