a = int(input('scrivere primo intero: '))
b = int(input('scrivere secondo intero: '))
c = int(input('scrivere terzo intero: '))
if a>=0 and b>=0 and c>=0 and a<b+c and b<a+c and c<a+b:
    if a!=b and a!=c and b!=a and b!=c and c!=a and c!=b:
        print('il triangolo è scaleno!')
    elif a==b and c!=a and c!=b or a==c and b!=a and b!=c or b==c and a!=b and a!=c:
        print('il triangolo è isoscele!')
    elif a==b and a==c and b==c:
        print('il triangolo è equilatero!')
else:
    print('input non valido')
