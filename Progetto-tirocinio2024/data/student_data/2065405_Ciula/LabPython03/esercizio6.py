s=input("Inserisci una stringa: ")
i=0
while(i<=(len(s)-1)):
    if(ord(s[i])<=100):
        o="stringa consumata e carattere non trovato"
        i+=1
    else:
        o="Il primo caattere con codice Unicode maggiore di 100 è "+s[i]
        break
print(o)

