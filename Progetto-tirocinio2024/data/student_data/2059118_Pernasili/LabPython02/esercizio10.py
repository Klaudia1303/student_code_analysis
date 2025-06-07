etc = float(input("Quanti anni ha il cane: "))
annidopo = int
anniprima = int
if etc >= 0:
    annidopo = etc-2
    anniprima = etc-annidopo
    print("In anni umani il cane ha", anniprima*10.50+annidopo*4)
if etc < 0:
    print("Errore")
