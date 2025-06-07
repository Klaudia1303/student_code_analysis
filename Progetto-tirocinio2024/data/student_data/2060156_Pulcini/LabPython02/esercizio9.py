m=int(input('mese'))
a=int(input('anno'))
if 1<=m<12:
    print((m+1),a)
elif m==12:
    print(1,(a+1))
elif m>12:
    print('input non valido')
    
