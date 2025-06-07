mese = int(input("Inserisci un mese: "))
if mese == 12 :
   mese = 0 
anno = int(input("Inserisci un anno: "))
if mese>= 0 and mese <= 12: 
        print(mese+1)
        print(anno+1)                
if mese > 12:
    print("input non valido")
