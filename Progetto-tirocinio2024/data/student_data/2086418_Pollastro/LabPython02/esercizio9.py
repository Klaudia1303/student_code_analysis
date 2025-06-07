mese=int(input('inserire mese:'))
anno=int(input('inserire anno:'))
if mese<1 and mese>12:
    print('input non valido')
    
if 1<=mese<12:
    print(mese+1,anno)
if mese==12:
    print(1,anno+1)
