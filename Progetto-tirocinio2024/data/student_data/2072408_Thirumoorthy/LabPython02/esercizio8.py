a=int(input('inserisci i dati di ingresso'))
b=int(input('inserisci i dati di ingresso'))
c=int(input('inserisci i dati di ingresso'))
if (a>0) and (b>0) and (c>0):
    if a+b>c and b+c>a and a+c>b:
        if a==b==c:
            print('equilatero')
        elif a==b or a==c or b==c:
            print('isoscele')
        elif a!=b!=c:
            print('scaleno')
else:
    ('input non valido')
