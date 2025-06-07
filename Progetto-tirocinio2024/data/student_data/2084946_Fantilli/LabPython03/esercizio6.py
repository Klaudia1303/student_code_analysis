s = input()
i=0
while ord(s[i]) <= 100:
    i += 1
    if len(s)==i:
        print("Stringa consumata e carattere non trovato")
if ord(s[i]) > 100:
    print("Il primo carattere con codice Unicode maggiore di 100 è:", s[i])
    
    
