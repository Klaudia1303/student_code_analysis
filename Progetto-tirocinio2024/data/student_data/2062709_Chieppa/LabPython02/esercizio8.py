a=int(input('inserire valore a: '))
b=int(input('inserire valore b: '))
c=int(input('inserire valore b: '))
if a>0 and a<b+c and b>0 and b<a+c and c>0 and c<a+b:
    if a==b and b!=c or b==c and a!=c:
        print('isoscele')
    if a==b and b==c:
        print('equilatero')
    if a!=b and b!=c and a!=c:
        print('scaleno')
else: print('input non valido')
