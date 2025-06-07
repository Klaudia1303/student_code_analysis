a=int(input('Inserire un numero intero: '))
b=int(input('Inserire un secondo numero intero: '))
c=int(input('Inserire un terzo numero intero: '))
if (a>=0 and b>=0 and c>=0) and (a<b+c and b<a+c and c<a+b):
    if a!=b!=c:
        print('scaleno')
    if a==b!=c or a==c!=b or b==c!=a:
        print('isoscele')
    if a==b==c:
        print('equilatero')
else:
    print('input non valido')
