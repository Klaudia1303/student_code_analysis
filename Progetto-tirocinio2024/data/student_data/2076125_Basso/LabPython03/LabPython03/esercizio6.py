
a=input("Inserisci stringa:\t")
A=0
b=a[A]
c=ord(b)


while c <= 100 and A < (len(a)-1):
    
    A=(A+1)
    b=a[A]
    c=ord(b)
if c> 100:
    print("Il primo carattere con codice Unicode maggiore di 100 è",b)
else:
    print("stringa consumata e carattere non trovato")
