etac = float(input("inserisci l'età del cane: "))
if 0<etac<3:
    anno=10.5
    print("L'età del cane in età umana è: ",etac*10.5)
elif etac>2:
    etac=etac-2
    print("L'età del cane in età umana è: ", (4*etac)+21)
else:
    print("input non valido")

