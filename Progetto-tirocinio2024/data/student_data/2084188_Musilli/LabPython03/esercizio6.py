b=True
while b:
    s=input("Inserire  una stringa (il programma finisce quando la stringa\
finisce o quando vi è presente un carattere in UNICODE >100): ")
    if s!="": b=False
i=0
b=True
while i<len(s) and b:
    if ord(s[i])>100:
        print("Il primo carattere con codice UNICODE maggiore di 100 è ",s[i])
        b=False
    i+=1
if b:   print("Stringa consumata e carattere non trovato")
