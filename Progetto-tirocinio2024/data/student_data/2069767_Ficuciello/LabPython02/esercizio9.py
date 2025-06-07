m=int(input('Inserire un numero intero che sia un mese:' ))
a=int(input('Inserire un numero intero che sia un anno:' ))
if 1<=m<=12 and m<=11:
    print(m+1, a)
elif m==12:
        print('1', a+1)
else:
    print('input non valido')
    
