#4) Scrivere un programma python che chiede in input all’utente una sequenza di numeri interi, uno per uno
#in maniera iterativa, terminando la richiesta di inserimento in input quando viene immesso l’intero “0”, e
#stampa a schermo il risultato della somma dei soli interi divisibili per 3.
#Esempio:
#Inserendo in questo ordine gli interi “1”, “2”, “-6”, “9”, “0” il programma termina e stampa “3”
c=0
som=0
while True:

    n=int(input("inserisci un numero intero: "))
    if n == 0:
        print(som)
        break
    if n %3==0:
        som+=n
        
