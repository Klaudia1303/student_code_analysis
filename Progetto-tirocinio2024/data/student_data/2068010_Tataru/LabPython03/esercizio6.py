s=input()
con=False
for i in s:
    if (ord(i)>100):
        print("Il primo carattere con codice Unicode maggiore di 100 è "+i)
        con=True
        break
if (con==False):
    print("stringa consumata e carattere non trovato")
