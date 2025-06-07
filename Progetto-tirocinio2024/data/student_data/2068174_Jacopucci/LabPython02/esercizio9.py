mese=input('inserire il mese: ')
mese=int(mese)
anno=input('inserire l\'anno: ')
anno=int(anno)
if(mese>=1 and mese <=12):
    if (mese+1>12):
        mese=1
        print(mese)
        print(anno)
    else:
        print(mese+1)
        print(anno)
else:
    print('input non valido')
