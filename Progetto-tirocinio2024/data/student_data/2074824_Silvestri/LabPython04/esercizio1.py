#Scrivere un programma python che chiede in input all’utente una
#sequenza di stringhe, una per una in
#maniera iterativa, terminando la richiesta di inserimento in input
#quando viene immessa una stringa
#contenente sia il carattere ‘a’ che il carattere ‘c’, e stampa il
#numero di stringhe lette (inclusa l’ultima).Esempio:
#• Inserendo in questo ordine le stringhe “pippo”, “albero”, “casa”
#il programma termina stampando “3”
a=input("Inserisci una stringa:")
count=1
while ('a'not in a) or ('c' not in a):
    count+=1
    a=input("Inserisci una stringa:")
    if 'a' in a and 'c'in a :
        print("Il ciclo è finito")
print(count)
