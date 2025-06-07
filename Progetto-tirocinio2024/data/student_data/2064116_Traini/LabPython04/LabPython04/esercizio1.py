#Scrivere un programma python che chiede in input all’utente una sequenza di stringhe, una per una in 
#maniera iterativa, terminando la richiesta di inserimento in input quando viene immessa una stringa
#contenente sia il carattere ‘a’ che il carattere ‘c’, e stampa il numero di stringhe lette (inclusa l’ultima).
#Esempio:
#• Inserendo in questo ordine le stringhe “pippo”, “albero”, “casa” il programma termina 
#stampando “3”
n=str(input('inserire un stringa (inserire stringhe contenenti "a" e "c" per terminare): '))

a='a'
c='c'

i=0


while  a and c not in n:
    n=str(input('inserire un stringa (inserire stringhe contenenti "a" e "c" per terminare): '))

    n.find(a)
    n.find(c)
    i=i+1
if a and c in n:
    i=i+1
    print(i)
    
    
