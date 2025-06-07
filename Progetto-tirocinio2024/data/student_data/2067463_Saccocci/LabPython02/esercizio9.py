m=int(input('Inserire mese:'))
a=int(input('Inserire anno:'))
ms=m+1
if 1<=m<=12:
    if ms!=13:
        print(ms,a)
    elif ms==13:
        print(1,a+1)
else:print('input non valido')
