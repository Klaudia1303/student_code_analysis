a=int(input('inserisci mese: '))
b=int(input('inserisci anno: '))
if 1<=a<=12:
    if a==12:
        print('1 ' + str(b))
    else:
        print(str(a+1) + ' ' + str(b))
else:
    print('input non valido')
