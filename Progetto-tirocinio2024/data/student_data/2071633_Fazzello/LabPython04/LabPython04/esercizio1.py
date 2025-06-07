##1) Scrivere un programma python che chiede in input all’utente una sequenza di stringhe, una per una in
##maniera iterativa, terminando la richiesta di inserimento in input quando viene immessa una stringa
##contenente sia il carattere ‘a’ che il carattere ‘c’, e stampa il numero di stringhe lette (inclusa l’ultima).
##Esempio:
##• Inserendo in questo ordine le stringhe “pippo”, “albero”, “casa” il programma termina
###stampando “3”
s=''
n=0
while s.find('a')==-1 or s.find('c')==-1: 
    s=input('inserire una stringa: ')
    n=n+1
print(n)
