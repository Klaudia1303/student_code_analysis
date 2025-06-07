Mese= int(input("inserisci il numero del mese:"))
Anno= int(input("inserisci l'anno:"))
if Mese<1 or Mese>12:
    print("input non valido")
elif Mese>=1 and Mese<12:
    print(Mese+1,Anno)
elif Mese==12:
    print("1",Anno+1)
