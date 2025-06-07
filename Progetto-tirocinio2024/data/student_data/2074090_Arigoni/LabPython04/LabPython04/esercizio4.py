s=input("Inserisci un intero (* per terminare) ")
somma=0
while s!="*":
    if int(s)!=0 and int(s)%3==0:
        somma=somma+int(s)
    print("somma parziale= ",somma)
    s=input("Inserisci un intero (* per terminare) ")
print("totale = ",somma)
