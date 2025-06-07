etaCane = float(input("Inserisci l'età del cane: "))
if etaCane >= 0:
    if etaCane == 1:
        etaUmana = 10.5
    else:
        if etaCane == 2:
            etaUmana = 21
        else:
            etaUmana = 21 + ((etaCane - 2) * 4)
    print("Età del cane convertita in età umana: ", etaUmana)
else:
    print("Input non valido.")
