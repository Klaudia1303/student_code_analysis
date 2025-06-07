mese = int(input("inserisci il mese: "))
anno = int(input("inserisci l'anno: "))

if mese > 12 or mese < 1:
    print("input non valido")
elif mese+1 == 13:
    print(mese-11, anno+1)
else:
    print(mese+1, anno+1)
