#Scrivere un programma che chiede in input all’utente di inserire una stringa palindroma, e nel caso in cui
#la stringa inserita non sia palindroma continua a chiedere l’inserimento di una stringa palindroma. Il
#programma termina all’inserimento della stringa palindroma e stampa la il messaggio “stringa
#palindroma di lunghezza ”, seguito dalla lunghezza della stringa. Esempio
#•
#Inserendo la stringa “arcobaleno” il programma stampa “non palindroma, inserire una stringa
#palindroma: ”; inserendo successivamente “mamma’” il programma stampa “non palindroma,
#inserire una stringa palindroma”; inserendo ‘
s=input("Inserisci una stringa : ")
a=0
b=len(s)

i=0
while i<len(s)/2:
    a+=1
    b-=1
    if s[a]!=s[b]:
        i=0
        s=input("non palindroma, inserire una stringa palindroma: ")
    i+=1

    
print("stringa palindroma di lunghezza ", len(s))
