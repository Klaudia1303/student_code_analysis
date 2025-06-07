##3) Scrivere un programma python che chiede in input all`utente una sequenza di numeri interi, uno per
##uno in maniera iterativa terminando la richiesta di inserimento in input quando viene immesso il
##carattere ‘*’ (asterisco), e stampa a schermo la somma dei soli interi negativi.
##Esempio:
##• Inserendo gli interi “14”, “-4”, “-7”, “22” e infine il carattere “*”, il programma stampa “-11”
##• Inserendo gli interi “5” “-5” e infine il carattere “*”, il programma stampa “-5”

n=0
s=1
while s!='*':
    s=(input('inserire un numero intero, * per terminare: '))
    if s!='*':
        s=int(s)
        if s<0:
             n=n+s
print('somma numeri negativi:',n)
    
