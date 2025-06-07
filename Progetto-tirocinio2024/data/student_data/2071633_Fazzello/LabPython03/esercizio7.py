#7) Scrivere un programma python che chiede in input all’utente un carattere c e una sequenza di stringhe,
#una per una in maniera iterativa, terminando la richiesta di inserimento in input quando il carattere c
#compare più di 2 volte nella stringa inserita in input. Prima di terminare il programma stampa il numero
#di occorrenze di c nell’ultima stringa inserita. Esempio:
#• Inserendo in questo ordine il carattere “t” e le seguenti stringhe, “atto”, “arto” e “architettata” il
#programma termina stampando “4”
#• Inserendo in questo ordine il carattere “b” e le seguenti stringhe, “bingo” e “obbrobrio”, il
#programma termina stampando “3”

c=input("Inserisci un carattere ")
c=str(c)
s=input("Inserisci una stringa ")
while s.count(c)<=2:
    s=input("Inserisci una stringa ")
print (s.count(c))
