m = int(input("Inserisci il mese: "))
a = int(input("Inserisci l'anno: "))
if m >= 1 and m <= 12:
    if m == 12:
        print("Mese successivo: 1", a + 1)
    else:
        print("Mese successivo: ", m + 1, a)
else:
    print("Input non valido.")
