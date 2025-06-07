n=input("Inserisci un numero poitivo o negativo: ")
somma=0
ris="-"
while n!="*":
    if n[0]=="-":
        somma=somma+int(n[1])
    n=input("Inserisci un numero poitivo o negativo: ")
print(str(ris)+str(somma))
