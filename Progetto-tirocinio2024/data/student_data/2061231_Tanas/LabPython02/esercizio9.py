mese = int(input("mese: "))
anno = int(input("anno: "))
if not 1 <= mese <= 12:
    print("input non valido")
else:
    mese += 1
    if mese > 12:
        mese = 1
        anno += 1
    print(str(mese), str(anno))
