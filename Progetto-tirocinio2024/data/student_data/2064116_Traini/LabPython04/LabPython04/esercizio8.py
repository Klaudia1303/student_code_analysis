#Scrivere un programma che prende in ingresso una sequenza di stringhe, una per una in maniera iterativa, 
#e termina la richiesta di inserimento in input quando l’ultimo carattere della stringa precedente è uguale 
#al primo carattere di quella attuale. Prima di terminare il programma stampa su un'unica riga le ultime 
#due stringhe inserite, separate da uno spazio. 
#Esempio:
#• Inserendo in questo ordine le stringhe “pippo”, “casa”, “albero”, il programma termina stampando 
#“casa albero”.
i=0
cn=0
while i!=1:
    while cn<1:
        s=input('inserire una stringa non vuota: ')
        c=str(s)
        k=str(' ')
        cn+=1
        while cn>=1 and i!=1:
            sc=input('inserire una stringa non vuota: ')
            k=str(sc)
            if k[0]==c[-1]:
                print(c,k)
                i+=1
            s=input('inserire una stringa non vuota: ')
            c=str(s)
            if k[-1]==c[0]:
                print(k,c)
                i+=1
    
        
