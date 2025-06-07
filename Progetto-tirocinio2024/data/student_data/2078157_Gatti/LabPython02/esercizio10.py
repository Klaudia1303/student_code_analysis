#esercizio 10
a =  float(input('inserisci l\'età del cane: '))
if a>0:
    if a<=2:
        print('l\'età dell\'uomo corrispondente è: ', 10.5*a)
    else:
        print('l\'età dell\'uomo corrispondente è: ', 10.5*2+4*(a-2))
else:
    print('input non valido')
