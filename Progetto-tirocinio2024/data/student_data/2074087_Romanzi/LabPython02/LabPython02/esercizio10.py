c=float(input('Età cane '))
if c<0:
    print('Input non valido')
else:
    if c<=2:
        print('Anni uomo '+str(c*10.5))
    else:
        print('Anni uomo '+str(21+(c-2)*4))
