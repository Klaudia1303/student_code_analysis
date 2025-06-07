mese=int(input("inserisci un mese: "))
while mese>12 or mese==0:
    mese=int(input("il mese deve essere compreso tra 1 e 12: "))
anno=int(input("inserisci un anno: "))
if mese==12:
    mese=1
    print(mese,anno+1)
else:
    print(mese,anno)
