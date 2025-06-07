#Scrivere un programma python che chiede in input all`utente una sequenza di numeri interi, uno per
#uno in maniera iterativa terminando la richiesta di inserimento in input quando viene immesso il
#carattere ‘*’ (asterisco), e stampa a schermo la somma dei soli interi negativi.
#Esempio:
#• Inserendo gli interi “14”, “-4”, “-7”, “22” e infine il carattere “*”, il programma stampa “-11”
#• Inserendo gli interi “5” “-5” e infine il carattere “*”, il programma stampa “-5”
c=0
som=0
while True:

    n=input("inserisci un numero intero: ")
    if n == "*":
        print(som)
        break
    if int(n) <0:
        som+=int(n)
        
