m=int(input('inserire un mese: '))
a=int(input('inserire un anno: '))
m>=1 and m<=12
if m<1 or m>12:
    print('input non valido')
r_m=m+1
if r_m<=12:
    print(r_m)
elif r_m+1>12:
    print(1)
if r_m+1>12:
    print(a+1)
elif r_m+1<=12:
    print(a)
