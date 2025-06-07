mese=int(input('inserire un mese: '))
anno=int(input('inserire un ann0: '))
if (mese>=1 and mese<=12):
    if mese==12:
        mese=1
        anno+=1
    else:
        mese+=1
    print(mese,anno)
else:
    print('non valido')
