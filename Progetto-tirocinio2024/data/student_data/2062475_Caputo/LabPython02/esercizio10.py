etac = float(input("inserire l'età del cane: "))
if (etac > 0):
    if (etac >= 2):
        etaum = (10.5 * 2) + ((etac - 2)*4)
        print ("la sua età umana corrisponde a:", etaum,"anni")
    elif (etac < 2):
        etaum = 10.5 * etac
        print ("la sua età umana corisponde a:", etaum,"anni")
else:
    print ("input non valido")
