m=int(input("inserire numero del mese: "))
a=int(input("inserire numero dell\'anno: "))
if 1<=m<=12:
    if m==12:
        print(m-11,a+1)
    else:
        print(m+1,a)
else:
    print('input non valido')
