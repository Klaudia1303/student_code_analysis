mese = int(input("Inserisci numero mese --> "))
while(mese<1 or mese>12):
    mese = int(input("Inserisci numero mese corretto --> "))
anno = int(input("Insersici anno --> "))
if(mese<12):
    print((mese+1),anno)
else:
    print("1",(anno+1))
