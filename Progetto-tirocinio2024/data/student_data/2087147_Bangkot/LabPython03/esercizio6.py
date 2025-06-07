s=input()
i=0
while ord(s[i])>chr(100):
    i+=1
    if ord(s[i])>=chr(100):
        print("Il primo carattere con codice Unicode maggiore di 100 è:",str(chr(i)))
    else:
        print("stringa consumata e carattere non trovato")
