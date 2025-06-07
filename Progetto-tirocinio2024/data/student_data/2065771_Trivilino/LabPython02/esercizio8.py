a=int(input('Inserire un intero: '))
b=int(input('Inserire un secondo intero: '))
c=int(input('Inserire un terzo intero: '))
if a<=0 or b<=0 or c<=0 or a>b+c or b>a+c or c>a+b:
      print('Input non valido')
else:
    if a==b and a==c:
        print ('Triangolo equilatero')
    elif a==b or b==c or a==c:
        print ('Triangolo isoscele')
    else:
        print ('Triangolo scaleno')
