mese = int(input('Inserire un mese:'))
anno = int(input('Inserire un anno:'))

if 1 <= mese < 12:
    print(mese+1, anno)
elif mese == 12:
    print(1, anno+1)
elif mese >= 13:
    print('input non valido')
