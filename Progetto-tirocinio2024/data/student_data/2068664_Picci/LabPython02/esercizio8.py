a = int(input('inserisci intero a: '))
b = int(input('inserisci intero b: '))
c = int(input('inserisci intero c: '))
if a>0 and b>0 and c>0 and a<b+c and b<a+c and c<a+b and a!=b and a!=c and b!=c:
    print('scaleno')
if a>0 and b>0 and c>0 and a<b+c and b<a+c and c<a+b and a==b and a!=c and b!=c:
    print('isoscele')
if a>0 and b>0 and c>0 and a<b+c and b<a+c and c<a+b and a==b and a==c and b==c:
    print('equilatero')
if a<0 or b<0 or c<0 or a>b+c or b>a+c or c>a+b:
    print('input non valido')
