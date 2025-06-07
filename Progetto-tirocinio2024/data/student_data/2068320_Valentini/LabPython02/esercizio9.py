mese= int(input("inserire un mese: "))
anno= int(input("inserire un anno: "))
mese2= mese+1
anno2= anno+1
if int(mese)>12:
    print("input non valido")
else:
    if int(mese)==12:
        print("01/"+str(anno2))
    else:
        print(str(mese2)+"/"+str(anno))
