mese=int(input("Inserisci il mese: "))
anno=int(input("Inserisci l'anno: "))
var=False
if mese>=1 and mese<=12:
    var=True
else:
    print("input non valido")

if var==True:
    if mese==12:
        print("1",anno+1)
    else:
        print(mese,anno)
