s=input("Inserisci una stringa di almeno 1 carattere: ")
i=0
while i<=len(s)-1:
    if ord(s[i])>100:
           print("Il primo carattere con codice Unicode maggiore di 100 è: "+s[i])
           break
    i +=1
if i==len(s):
    print("stringa consumata e carattere non trovato")
           
