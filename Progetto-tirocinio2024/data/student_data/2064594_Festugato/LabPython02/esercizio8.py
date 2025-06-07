a = int(input('lato 1: '))
b = int(input('lato 2: '))
c = int(input('lato 3: '))
if a > 0 and b>0 and c>0 and a<(b+c) and b<(c+a) and c<(a+b):
    if a!=b and a!=c and b!=c:
        print('scaleno')
    elif a==b and a!=c:
        print('isoscele')
    elif a==c and a!=b:
        print('isoscele')
    elif b==c and b!=a:
        print('isoscele')
    elif a==b==c:
        print('equilatero')
else:
    print('input non valido')

    

    
    
    
    
