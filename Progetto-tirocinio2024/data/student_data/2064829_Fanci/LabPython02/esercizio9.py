mese = int(input("inserisci mese: "))
anno = int(input("inserisci anno: "))
if 0<mese<12:
           print("mese anno: ",mese+1,anno+1)
elif mese==12:
    mese=1
    print("mese anno: ",mese, anno+1)
else:
    print("input non valido")
