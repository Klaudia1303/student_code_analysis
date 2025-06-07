s=input("inserisci")
i=0
while i<len(s):
    if ord(s[i])<=100:
        i=i+1
    else:
        print("il carattere ",s[i]," ha codice Unicode maggiore di 100")
        break
if i==len(s):
    print("stringa consumata e carattere non trovato")
    
