s = input ('Inserisci una stringa composta da almeno un carattere :')
leng = len(s)-1
i = 0
while i<= leng :
    if ord(s[i])>100:
        print ('Il primo carattere con codice Unicode maggiore di 100 è ',s[i])
        i= leng+1
    elif i==leng:
        print ('Stringa consumata e carattere non trovato')
    i=i+1
