s=input("Inserire la stringa")
i=0
while(i<len(s)-1 and ord(s[i])<=100):
    print s[i]
    i+=1
if (ord(i)>100):
    print("Il primo carattere con codice Unicode maggiore di 100 e'",s[i])
else:
    print("Stringa consumata carattere non trovato")
