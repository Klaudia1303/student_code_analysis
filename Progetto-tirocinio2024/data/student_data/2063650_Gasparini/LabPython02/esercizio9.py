mese = int(input("Mese: "))
anno = int(input("Anno: "))
if mese < 1 or mese > 12:
    print("input non valido")
else:
    if mese == 12:
        mese = 1
        anno += 1
    else:
        mese += 1
    print(mese, anno)
