a=int(input('Primo numero intero: '))
b=int(input('Secondo numero intero: '))
c=int(input('Terzo numero intero: '))
if a>0 and b>0 and c>0 and a+b>c and a+c>b and b+c>a:
    if a==b==c:
        print('equilatero')
    else:
        if a==b or a==c or b==c:
            print('isoscele')
        else:
            print('scaleno')
else:
    print('input non valido')
