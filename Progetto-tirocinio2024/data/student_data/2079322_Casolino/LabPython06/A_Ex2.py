#Diciamo che una stringa è palindroma di livello 1 se il primo e
#ultimo carattere sono uguali, di livello 2 se il primo è uguale all’ultimo e
#il secondo al penultimo, e così via. Scrivere un programma Python che prende
#in input una stringa s e calcola il livello massimo di palindromicità della
#stringa. Ad esempio, se la stringa s vale ‘alidfefcila’ allora il livello è 3.
#Se la stringa è palindroma allora il suo livello deve essere uguale
#alla sua lunghezza.

s = str(input("Inserire una stringa: "))
posizione_c=1
livello=0
for i in range(int(len(s)/2)): # /2 perchè devo arrivare a spezzare la stringa a metà
    if s[i]==s[len(s)-posizione_c]: #all'inizio controllo la posizione len(s)-1
                                    #perchè le posizioni dei caratteri partono
                                    #da 0 e sono len(s)-1
        livello+=1
        posizione_c+=1
    else:
        break
print("Il livello massimo di palindromicità della stringa è: ",livello)
        
    
