s=input("Inserisci una stringa: ")

i=0

print(len(s))

while(i<len(s)):
    
    if(ord(s[i]) > 100):
        print("Il primo carattere con codice Unicode maggiore di 100 è", s[i])
        break
    
    if i==(len(s)-1):
        print("stringa consumata e carattere non trovato\n")
    
    i+=1



