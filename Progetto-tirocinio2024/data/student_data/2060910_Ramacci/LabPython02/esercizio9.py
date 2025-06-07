mese=int(input("inserire numero mese: "))
anno=int(input("inserire numero anno: "))
if mese>=1 and mese<12:
    print(mese+1, anno)
elif mese==12:
    print("1", anno+1)
elif mese<1 or mese>12:
    print("input non valido")
