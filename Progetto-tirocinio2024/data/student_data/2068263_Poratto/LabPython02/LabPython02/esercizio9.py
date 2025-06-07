x=int(input('inserisci il valore di un mese tra 1 e 12: '))
x1=int(input('inserisci un anno: '))
if 1<=x<=12:
    if 1<=x<=11:
        Ris=x+1
        print((Ris),end=' ')
        print(x1)
    else:
        x==12
        print(('1'),end=' ')
        print(x1+1)
else:
    x>12
    print('Valore non valido')

