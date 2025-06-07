s=input("inserisci stringa di almeno un carattere")
n=0
corretto=False
while not corretto:
    if ord(s[n])>100:
        print("Il primo carattere con codice Unicode maggiore di 100 è "+s[n])
        corretto=True
    n+=1
    if n>len(s)-1:
        print("stringa consumata e carattere non trovato" )
        corretto=True
   
    
