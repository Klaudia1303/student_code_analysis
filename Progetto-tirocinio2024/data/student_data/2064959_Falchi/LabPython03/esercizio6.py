s = input("Inserire stringa: ")
i = 0

found = False

while i < len(s):
    if not (ord(s[i:i+1]) < 100):
        found = True
        print("Il primo carattere con codice Unicode maggiore di 100 è", s[i:i+1])
        i = len(s) #Interrompe il ciclo while.
    i = i + 1

if not found:
    print("stringa consumata e carattere non trovato")        
