a=int(input('numero intero'))
b=int(input('numero intero'))
c=int(input('numero intero'))

if a>0 and b>0 and c>0 and a<b+c and b<a+c and c<a+b:
    print('il triangolo esiste')
else:
    print('input non valido')
if a==b==c:
    print('equilatero')
elif a==b or b==c or c==a:
    print('isosciele')
else:
    print('scaleno')
