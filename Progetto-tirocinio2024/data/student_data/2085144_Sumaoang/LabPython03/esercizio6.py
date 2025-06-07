
s = input("inserisci la stringa: ")

i = 0

carattereDaMemorizzare = ""

while i < len(s):
    carattere = s[i]
    if ord(carattere) > 100 and carattereDaMemorizzare == "":
        carattereDaMemorizzare = carattere
    i+=1

if carattereDaMemorizzare != "":
    print("Il primo carattere con codice Unicode maggiore di 100 è " + carattereDaMemorizzare)
else:
    print("stringa consumata e carattere non trovato") 
