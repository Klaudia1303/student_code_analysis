# Scrivere un programma python che chiede in input all’utente una sequenza di numeri interi, uno per 
#uno in maniera iterativa terminando la richiesta di inserimento in input quando viene immesso il 
#carattere “*” (asterisco), e stampa a schermo quanti interi positivi sono stati inseriti. 
#Esempio:
#• Inserendo gli interi “4”, “-5”, “-6”, “3” e infine il carattere “*”, il programma stampa “2”
#• Inserendo gli interi “-5” “-5” e infine il carattere “*”, il programma stampa “0”


n=input('inserire un intero (* per terminare): ')
i=0
s=int(n)
while n!='*':
    if s>0:
        n=input('inserire un intero (* per terminare): ')
        i=i+1
    if s<0:
        n=input('inserire un intero (* per terminare): ')
        i=i-1
if n=='*':
    print(i)
