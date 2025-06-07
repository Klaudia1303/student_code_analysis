#7) Scrivere un programma python che chiede in input all’utente una stringa s e stampa a schermo il
#carattere che compare più volte in s. Se c’è più di un carattere con queste caratteristiche, stampare quello
#che
#fra
#questi
#compare
#per
#ultimo
#nella
#stringa
#(da
#sinistra
#a
#destra).
#Esempio:
#• Inserendo la stringa “pippo”, il programma deve stampare “p”
#• Inserendo la stringa “clarabella”, il programma deve stampare “a” (sia ‘a’ che ‘l’ compaiono 3
#volte, che è il massimo numero di volte in cui compare un carattere nella stringa, e c’è una
#occorrenza di ‘a’ che segue tutte le occorrenze di ‘l’, per cui ‘a’ compare per ultimo)
#Nota: Si assuma che la stringa s in input non sia mai la stringa vuota.

s=input("inserisci una stringa : ")
i=0
c=0
j=0
char=""
while i<len(s):
    c=s.count(s[i])
    if c >= j:
        j=c
        char=s[i]
    i+=1

print(char)
    
