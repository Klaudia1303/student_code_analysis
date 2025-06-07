s=input("inserisci una stringa")
i=0
while i<len(s)-1 and ord(s[i])<=100:
    i+=1
if ord(s[i])>100:
    print("Il primo carattere con codice Unicode maggiore di 100 è",s[i])
else:
    print("Stringa consumata e carattere non trovato")
