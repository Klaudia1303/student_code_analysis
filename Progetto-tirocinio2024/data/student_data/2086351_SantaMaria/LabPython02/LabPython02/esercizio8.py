a=int(input('Inserisci un intero: '))
b=int(input('Inserisci un secondo intero: '))
c=int(input('Inserisci un terzo intero: '))
if a>0 and b>0 and c>0 and a<b+c and b<a+c and c<a+b:
    if a!=b and b!=c and c!=a:
        print('scaleno')
    elif a==b and b!=c and a!=c or b==c and a!=b and c!=a or c==a and a!=b and b!=c:
        print('isoscele')
    else:
        a==b and b==c and c==a
        print('equilatero')
else:
    print('input non valido')
