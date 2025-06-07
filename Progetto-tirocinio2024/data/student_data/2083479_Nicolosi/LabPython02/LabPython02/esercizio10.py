età=int(input('Inserisci l\'età del cane: '))
if età==1:
    print(10.5)
elif età==2:
    print(21)
elif età>2:
    print(21+((età-2)*4))
elif età<1:
    print('Input non valido')