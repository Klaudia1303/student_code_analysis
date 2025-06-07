##4) Scrivere un programma python che chiede in input all’utente una sequenza di numeri interi, uno per uno
##in maniera iterativa, terminando la richiesta di inserimento in input quando viene immesso l’intero “0”, e
##stampa a schermo il risultato della somma dei soli interi divisibili per 3.
##Esempio:
##Inserendo in questo ordine gli interi “1”, “2”, “-6”, “9”, “0” il programma termina e stampa “3”

n=''
m=0
while n!=0:
    n=int(input('inserire un numero intero: '))
    if n%3==0:
        m=m+n
print(m)
