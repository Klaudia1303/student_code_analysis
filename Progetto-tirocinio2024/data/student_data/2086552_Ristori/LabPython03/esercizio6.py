var1=str(input("Inserire una stringa composta da almeno un carattere:"))
b=True
j=0
while b:
    j=j+1
    if j>len(var1)-1:
        print("Stringa consumata e carattere non trovato")
        b=False
    elif ord(var1[j])>100:
        print("Il primo carattere con codice Unicode maggiore di 100 è:",var1[j])
        b=False
    
