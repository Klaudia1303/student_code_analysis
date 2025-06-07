a=int(input('Inserisci il primo intero '))
b=int(input('Inserisci il secondo intero '))
c=int(input('Inserisci il terzo intero '))
if (a>0 and b>0 and c>0 and a+b>c and a+c>b and b+c>
    a):
    if (a==b==c):
        print('equilattero')
    elif(a==b!=c or a==c!=b or b==c!=a):
        print('isoscele')
    elif(a!=b!=c):
        print('scaleno')
else:
    print('Input non valido')
    
