s=input("Inserire una stringa: ")
l=int(len(s)-1)
i=0
while i<=l:
    if ord(s[i])>100:
        print("Il primo carattere con codice Unicode maggiore di 100 è "+str(s[i]))
        break
    i=i+1
if i>l:
    print("Stringa consumata e carattere non trovato.")
