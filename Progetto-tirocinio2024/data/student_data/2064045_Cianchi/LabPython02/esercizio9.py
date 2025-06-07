m=input('inserire un mese:')
m=int(m)
a=input('inserire un anno:')
a=int(a)
if m<1 or m>12:
    print('input non valido')
if m==12:
    print(1,a+1)
else:
    print(m+1,a)
