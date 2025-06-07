s = str(input("inserisci una stringa: "))
x = len(s)
i = 0
while (i<x and int(ord(s[i])<=100)):
    i += 1
if i == x:
    print("stringa consumata e carattere non trovato")
else:
    print("Il primo carattere con codice Unicode maggiore di 100 è: " +s[i])

