
#Scrivere un programma python che chiede in input all’utente una sequenza di stringhe, una per una inmaniera iterativa, terminando la richiesta di inserimento in input quando viene immessa una stringa
#fatta esclusivamente da caratteri alfabetici minuscoli (quindi anche senza spazi) e stampa per ogni
#stringa il primo e l’ultimo carattere. Si assuma che l’utente non inserisca mai la stringa vuota. Si
#ricorda che, data una stringa s, (i) l’istruzione s.isalpha() restituisce True se s contiene solo
#caratteri alfabetici, altrimenti restituisce False, e che (ii) l’istruzione s.islower() restituisce
#True se s contiene almeno un carattere alfabetico minuscolo e nessun carattere alfabetico maiuscolo,
#altrimenti restituisce False. Esempio:
#•
#Inserendo in questo ordine le stringhe “Casa”, “esercitazione3” e “abaco”, il programma stampa
#“Ca”, e poi, dopo aver chiesto di inserire una nuova stringa, stampa
#“e3”,
#e,
#dopo
#aver
#chiesto
#di
#inserire
#una
#nuova
#stringa,
#stampa
#“ao” e termina.
bo=True
while bo:
    s=input("Inserisci una stringa : ")
    if s.islower() and s.isalpha():
        print(s);
        bo=False
    else:
        print(s[0]+s[-1])
        
