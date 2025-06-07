mese = int(input("inserire il mese: "))
anno = int(input("inserire l'anno: "))
if (mese >= 1 and mese <= 12):
    if (mese+1 > 12):
        print ("1", anno+1)
    else:
        print (mese+1, anno)
else:
    print ("input non valido")
