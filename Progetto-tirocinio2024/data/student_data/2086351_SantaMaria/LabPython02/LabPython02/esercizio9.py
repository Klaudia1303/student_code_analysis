m=int(input('Inserisci un mese: '))
a=int(input('Inserisci un anno: '))
if 1<=m<=12:
    if m==12:
        print(1,a+1)
    else:
        print(m+1,a)
else:
    print('input non valido')
