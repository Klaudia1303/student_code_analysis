mese=int(input('inserisci il mese '))
anno=int(input('inserisci l\'anno '))
if(mese!=12 and mese<=12 and mese<1):
    print (mese+1,' ', anno)
elif(mese==12):
    print('1 ',anno+1)
else:
    print('Input non valido')
