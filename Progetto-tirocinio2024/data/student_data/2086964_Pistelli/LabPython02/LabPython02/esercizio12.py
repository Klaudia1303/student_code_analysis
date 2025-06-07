a=float(input('inserisci il numero della temperartura'))
b=str(input("inserisci l'unità di misura della temperatura(c o f)"))
c=(a-32)/(1.8)
if b!='c' and b!='f':
    print('errore')
elif b=='c' or b=='C':
    if a<=0:
        print('solida')
    elif 0<a<100:
        print('liquida')
    else:
        print('gassosa')
elif b=='f' or b=='F':
    if c<=0:
        print('solida')
    elif 0<c<100:
        print('liquida')
    else:
        print('gassosa')

