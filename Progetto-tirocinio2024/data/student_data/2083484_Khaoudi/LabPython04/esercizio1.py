#Scrivere un programma python che chiede in input all’utente una sequenza di stringhe, una per una in
#maniera iterativa, terminando la richiesta di inserimento in input quando viene immessa una stringa
#contenente sia il carattere ‘a’ che il carattere ‘c’, e stampa il numero di stringhe lette (inclusa l’ultima).
#Esempio:
#• Inserendo in questo ordine le stringhe “pippo”, “albero”, “casa” il programma termina
#stampando “3”
while True:
    stringa=input("inserisci una stringa : ")
    i=0
    c=0

    if stringa.index("c")!=-1 and stringa.index("a") != -1:
        while i<len(stringa) and c<2:
            if stringa[i]=="c" or stringa[i]=="a":
                c+=1
            i+=1
    break
print(i)
            
        
            
