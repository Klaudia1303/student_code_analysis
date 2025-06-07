s=input("Inserire una stringa:   ")
i=0
c=False
while len(s)>i:
    a=ord(s[i])
    if a>100:
        print("Il primo carattere con codice Unicode maggiore di 100 è",s[i])
        i=len(s)
        c=True
    else:
        i=i+1
if c==False:
    print("stringa consumata e carattere non trovato")

