mese=int(input('Inserire mese: '))
anno=int(input('Inserire anno: '))
if mese>=1 and mese<=11:
    print(mese+1,anno)
elif mese==12:
        print('1',anno+1)
else: print('input non valido')
