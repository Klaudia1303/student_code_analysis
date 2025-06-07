s=input("Inserisci una stringa: ")
n=0
while n<=(len(s))-1:
    if ord(s[n])>100:
        print("Il primo carattere con codice Unicode maggiore di 100 è "+s[n])
        break
    else:
        n+=1
        if n==len(s)-1:
            print("stringa consumata e carattere non trovato")

        

        
