mese=int(input('Inserisci un intero che rappresenti un mese: '))
anno=int(input('Inserisci un intero che rappresenti un anno: '))
if 0<mese<12:
    print(mese,' ',anno)
elif mese==12:
    print(1,' ',(anno+1))
elif mese>12:
    print('Input non valido')