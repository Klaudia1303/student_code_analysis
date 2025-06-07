#esercizio 8
a = int(input('inserisci un intero: '))
b = int(input('inserisci un intero: '))
c = int(input('inserisci un intero: '))
if (a>0 and b>0 and c>0) and (a+b>c and a+c>b and b+c>a):
    if a==b and b==c:
        print('triangolo equilatero')
    elif ((a>b or b>a) and (c!=b and c!=a)) or ((a>c or c>a) and (b!=a and b!=c)) or ((b>c or c>b) and (a!=c and a!=b)):
        print('triangolo scaleno')
    else:
        print('triangolo isoscele')
else:
    print('input non valido')
