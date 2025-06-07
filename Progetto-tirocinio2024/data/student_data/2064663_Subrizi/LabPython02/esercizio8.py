a = int(input('Inserisci il valore del lato a del triangolo: '))
b = int(input('Inserisci il valore del lato b del triangolo: '))
c = int(input('Inserisci il valore del lato c del triangolo: '))

if a>0 and b>0 and c>0 and a<b+c and b<a+c and c<a+b:
    print('Questo è un triangolo:')

if a!=b and a!=c and b!=c:
        print('scaleno')
elif a==b and a!=c or a==c and a!=b or b==c and b!=a:
    print('isoscele')
elif a==b and a==c:
    print('equilatero')
else:
    print('Input non valido')
