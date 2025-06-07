m=int(input('mese: '))
a=int(input('anno: '))
r=(m+1, a)
if 1<=m<12:
    print(r)
elif m==12:
    print(1, a+1)
else:
    print('input non valido')
