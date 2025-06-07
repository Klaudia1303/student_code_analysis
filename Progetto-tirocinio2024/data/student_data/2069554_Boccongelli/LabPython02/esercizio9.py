mese = int(input('Inserisci un mese (mm)'))
anno = int(input('Inserisci un anno (yyyy)'))

if (mese > 0 and mese <= 12):
    if (mese <= 11):
        m = mese + 1
        a = anno
    else:
        m = 1
        a = anno + 1
    print(m, a)
else:
    print('input non valido')
