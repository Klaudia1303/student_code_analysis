mese=int(input('Inserire un numero intero che rappresenti un mese: '))
anno=int(input('Inserire un numero intero che rappresenti un anno: '))
mesesucc=mese+1
annosucc=anno+1
if mese>=1 and mese<12:
    print(mesesucc,anno)
elif mese==12:
    print(1,annosucc)
else:
    print('input non valido')
