#Scrivere un programma python che chiede in input all’utente una stringa composta da almeno un carattere
#e la scandisce carattere dopo carattere partendo dal primo, sino a quando o la stringa finisce o si incontra
#un carattere il cui codice Unicode è maggiore di 100. Il programma deve stampare su di una riga il motivo
#per cui è terminato. Ci sono due possibili motivi:
#- stringa consumata senza trovare il carattere. In questo caso il programma deve stampare “stringa
#consumata e carattere non trovato”
#- trovato carattere con codice Unicode maggiore di 100. In questo caso il programma deve stampare “Il
#primo carattere con codice Unicode maggiore di 100 è” seguito dalla stampa del carattere.
#Esempio:
#• inserendo la stringa “CONTE”, stampa “stringa consumata e carattere non trovato”
#• inserendo la stringa “abaco”, stampa “Il primo carattere con codice Unicode maggiore di 100 è o”
#• inserendo la stringa “adamo”, stampa “Il primo carattere con codice Unicode maggiore di 100 è
#m”
s=input("Inserisci una stringa : ");
i=0
while i<=len(s):
    if i== len(s):
        print("stringa consumata e carattere non trovato")
    elif ord(s[i])>100:
        print("Il primo carattere con codice Unicode maggiore di 100 è",s[i])
    i+=1;
