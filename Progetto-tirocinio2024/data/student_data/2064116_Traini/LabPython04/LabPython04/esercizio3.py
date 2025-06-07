#Scrivere un programma python che chiede in input all`utente una sequenza di numeri interi, uno per 
#uno in maniera iterativa terminando la richiesta di inserimento in input quando viene immesso il 
#careattere ‘*’ (asterisco), e stampa a schermo la somma dei soli interi negativi. 
#Esempio:
#• Inserendo gli interi “14”, “-4”, “-7”, “22” e infine il carattere “*”, il programma stampa “-11” 
#• Inserendo gli interi “5” “-5” e infine il carattere “*”, il programma stampa “-5”
n=input('inserire un intero(* per terminare): ')
i=0
s=int(n)
while n!='*':
    s=int(n)
    n=input('inserire un intero(* per terminare): ')

    if s<0:
        i=i+s


    
print(i)
    
