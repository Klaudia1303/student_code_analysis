mese = input("inserisci il mese: ")
mese = int(mese)
anno = input("inserisci l'anno: ")
anno = int(anno)

if 1 <= mese <= 12:
    if mese <= 11:
        print(mese + 1,anno)
    elif mese == 12:
        print(1, anno + 1)
else:   print("input non valido")
