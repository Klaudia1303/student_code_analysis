a=int(input('Inserire primo numero intero: '))
b=int(input('Inserire secondo numero intero: '))
c=int(input('Inserire terzo numero intero: '))
if(a>0 and b>0 and c>0 and a<b+c and b<c+a and c<a+b):
    if(a==b and b==c):
        print('Triangolo equilatero')
    else:
        if(a==b or b==c or c==a):
            print('Triangolo isoscele')
        else:
            print('Triangolo scaleno')
else:
    print('Input non valido')
            
