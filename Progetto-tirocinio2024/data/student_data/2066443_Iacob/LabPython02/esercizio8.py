a = input('Insert number here: ')
a = int(a)
b = input('Insert number here: ')
b = int(b)
c = input('Insert number here: ')
c = int(c)
if a>0 and b>0 and c>0:
    if a<b+c and b<a+c and c<a+b:
        if a!=b!=c:
            print('Scaleno')
        elif a==b==c:
            print('Equilatero')
        else: print('Isoscele')
else: print('Input non valido')

    
