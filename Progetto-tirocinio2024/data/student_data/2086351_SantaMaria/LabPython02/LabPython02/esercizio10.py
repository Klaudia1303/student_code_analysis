cane=float(input('Inserisci l\'età del cane: '))
if cane>=0:
    if cane<=2:
        print(10.5*cane)
    else:
        print((cane-2)*4+21)
else:
    print('input non valido')
