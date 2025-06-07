s=input("Immetti una stringa composta da almeno un carattere: ")
i=0
primo=False
while i<=len(s)-1 and not primo:
    if ord(s[i]) > 100:
        primo=True
        print("Il primo carattere con codice Unicode maggiore di 100 e'",s[i])
    i+=1
if not primo:
    print("stringa consumata e carattere non trovato")
