m=int(input('Inserire intero mese: '))
a=int(input('Inserire intero anno: '))
if(m>=1 and m<=12):
    if(m==12):
        m=1
        print(m,a+1)
    else:
        print(m+1,a)
else:
    print('Input non valido')
    
