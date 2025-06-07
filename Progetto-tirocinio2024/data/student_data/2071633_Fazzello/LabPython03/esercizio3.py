#3) Scrivere un programma python che chiede in input all’utente una sequenza di numeri interi, uno per
#uno in maniera iterativa terminando la richiesta di inserimento in input quando viene immesso un
#numero divisibile per 5. Prima di terminare, il programma stampa a schermo la divisione intera fra
#l’ultimo numero inserito e 5. Esempio:
#• Inserendo in questo ordine le stringhe “13”, “-19”, “11”, “7” e “-10”, il programma termina
#stampando “-2”

a=input ("Inserisci numero ")
a=int(a)
while not a%5==0:
    a=input ("Inserisci numero ")
    a=int(a)

if a//5:
    print (a//5)
