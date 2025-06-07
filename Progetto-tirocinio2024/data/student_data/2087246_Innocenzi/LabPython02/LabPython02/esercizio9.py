mese=int(input("Inserisci un numero intero corrispondente a un mese: "))
anno=int(input("Inserisci un numero intero corrispondente a un anno: "))

if(mese<=12 and mese>=1):
    print(mese+1, anno)
    
    if(mese==12):
        print(1, anno+1)

else:
    print("Input non valido")