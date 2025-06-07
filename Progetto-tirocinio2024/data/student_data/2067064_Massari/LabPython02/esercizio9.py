mese = int(input('scrivere un mese: '))
anno = int(input('scrivere un anno: '))
if mese>=1 and mese<=12:
    if mese<12:
        print('il mese successivo è: ',mese+1,'/',anno)
    elif mese==12:
        print('il mese successivo è: ',1,'/',anno+1)
else:
    print('input non valido!')
    
