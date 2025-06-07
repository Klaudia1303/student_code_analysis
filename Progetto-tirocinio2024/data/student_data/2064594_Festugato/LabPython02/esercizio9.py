anno = int(input('inserisci anno: '))
mese = int(input('inserisci mese: '))

if 0<mese<12: 
    print(mese+1,anno)
elif mese==12:
    print(1,anno+1)
else:
    print('input non valido')
