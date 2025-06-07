a=int(input('Inserisci un intero a '))
b=int(input('Inserisci un intero b '))
c=int(input('Inserisci un intero c '))
if a>0 and b>0 and c>0 and a+b>c and a+c>b and b+c>a:
    if a==b and b==c and c==a:
        print('Equilatero')
    elif a==b or b==c or c==a:
        print('Isoscele')
    elif a!=b and a!=c and b!=c:
        print('Scaleno')
else:
    print('Input non valido')
