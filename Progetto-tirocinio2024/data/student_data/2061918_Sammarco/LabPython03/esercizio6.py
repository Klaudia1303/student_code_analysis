s = input("inserisci stringa: ")
i = 0
corretto = True
while corretto and i<len(s):
    if ord(s[i]) > 100:
        corretto = False
        print("il primo carattere con codice Unicode maggiore di 100 è:", s[i])
    else:
        i += 1   
if corretto:
    print("Stringa consumata e carattere non trovato")
