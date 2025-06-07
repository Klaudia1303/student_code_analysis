acqua=float(input('inserire valore:'))
udm=str(input('inserire unità di misura:'))
if udm=='F':
    a=((acqua)-32/1.8)
    if a<=0:
        print('solida')
    elif 0<a<=100:
        print('liquida')
    else:
        print('gassosa')
if udm=='C':
    a=acqua
    if a<=0:
        print('solida')
    elif 0<a<=100:
        print('liquida')
    else:
        print('gassosa')
