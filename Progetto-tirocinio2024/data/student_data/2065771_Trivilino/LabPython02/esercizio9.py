mese=int(input('Inserire il numero corrispondente a un mese: '))
anno=int(input('Inserire un anno: '))
if mese>=1 and mese<=12:
    if mese==12:
         print (int('1'), anno+1)
    else:
         print(mese+1, anno)
else:
    print('Input non valido')
