a=float(input('Inserire il 1° lato del triangolo '))
b=float(input('Inserire il 2° lato del triangolo '))
c=float(input('Inserire il 3° lato del triangolo '))
if a==0 or b==0 or c==0 or a+b<c or b+c<a or c+a<b:
    print('input non valido')
elif a==b==c:
    print('equilatero')
elif a!=b and b!=c and c!=a:
    print('scaleno')
else:
    print('isoscele')
