m=int(input('inserire mese: '))
a=int(input('inserire anno: '))
if 1<=m<=12:
    print(m+1,a)
elif m==13:
        print(1,a)
else:
    print('input non valido')
