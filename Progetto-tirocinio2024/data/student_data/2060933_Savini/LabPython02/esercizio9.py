mese= int(input('inserisci mese: '))
anno= int(input('inserisci anno: '))
if mese>0 and mese<12:
    print(mese+1)
elif mese==12:
    print(1)
if mese==12:
    print(anno+1)
elif 1<mese<12:
    print(anno)
if (mese>12 or mese<1):
    print('input non valido')

