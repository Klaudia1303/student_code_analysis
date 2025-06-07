mese = int(input("Inserisci mese: "))
anno = int(input("Inserisci anno: "))
if 1<=mese<12:
    print(str(mese+1)+' '+str(anno+1))
elif mese==12:
    print('1'+' '+str(anno+1))
else:
    print("input non valido")
