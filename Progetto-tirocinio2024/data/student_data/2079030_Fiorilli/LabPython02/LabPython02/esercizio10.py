a=float(input('inserisci l\'età del cane: '))
if a<0:
    print ('input non valido')
elif a<2:
    print (a*10.5)
else:
    print(21+(a-2)*4)
