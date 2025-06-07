m= int(input('inerisci mese: '))
a = int(input('inserisci anno: '))

if 1<=m<=12:
    if 1<=m<12:
        print(m+1, a)
    else:
        print(m-11, a+1)
else:
    print('input non valido')
