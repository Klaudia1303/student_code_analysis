a=int(input('inserire anno: '))
b=int(input('inserire mese: '))

if (b==12):
    b=1
    print(b)
    print(b+1)

else:
    if (b>=1 and b<12):
        print(b+1)
        print(a)
    else:
        ('input non valido')
