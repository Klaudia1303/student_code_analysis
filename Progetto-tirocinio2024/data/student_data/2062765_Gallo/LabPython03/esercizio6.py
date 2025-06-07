s=str(input("Inserire stringa: "))
finito=False
i=0
while not finito:
    if i==len(s):
        print("stringa consumata e carattere non trovato")
        finito=True
    elif ord(s[i])<=100:
        i+=1
    else:
        print("Il primo carattere con codice Unicode maggiore di 100 è "+s[i])
        finito=True
        
    
    
    
