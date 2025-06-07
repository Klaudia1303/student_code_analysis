mese=int(input('inserire mese: '))
anno=int(input('inserire anno: '))
if(1<=mese<=12):
    if(mese<12):
        mese=mese+1
        print(mese, anno)
    elif(mese==12):
        mese=1
        anno=anno+1
        print(mese, anno)
else:
    print('input non valido')