m=int(input('Numero mese: '))
a=int(input('Anno: '))
if m<=12:
    if m==12:
        print('1',a+1)
    else:
        print(m+1,a)
else:
    print('input non valido')
