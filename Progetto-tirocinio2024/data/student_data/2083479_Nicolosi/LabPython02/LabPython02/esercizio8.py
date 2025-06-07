a=int(input('Inserisci un primo intero: '))
b=int(input('Inserisci un secondo intero: '))
c=int(input('Inserisci un terzo intero: '))
if (a>0 and b>0 and c>0) and (a<(b+c) and b<(a+c) and c<(a+b)) and (a!=b and b!=c and a!=c):
    print('Il triangolo è scaleno')
elif (a>0 and b>0 and c>0) and (a<(b+c) and b<(a+c) and c<(a+b)) and ((a==b and b!=c and a!=c) or (a!=b and b==c and a!=c) or (a!=b and b!=c and a==c)):
    print('Il triangolo è isoscele')
elif (a>0 and b>0 and c>0) and (a<(b+c) and b<(a+c) and c<(a+b)) and (a==b and b==c and a==c):
    print('Il triangolo è equilatero')
else:
    print('Input non valido')