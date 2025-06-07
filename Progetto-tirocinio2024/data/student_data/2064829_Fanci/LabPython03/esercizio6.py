s = input("inserisci stringa: ")
i = 0
if len(s)>0:
    sen=True
    while sen==True and len(s)>i:
        if ord(s[i])>100:
            print("Il primo carattere con codice Unicode maggiore di 100 è:",s[i])
            sen=False
        i+=1
    if sen==True:
         print("stringa consumata")
            
