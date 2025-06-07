#8) Scrivere un programma che chiede in input all’utente di inserire una stringa palindroma, e nel caso in cui
#la stringa inserita non sia palindroma continua a chiedere l’inserimento di una stringa palindroma. Il
#programma termina all’inserimento della stringa palindroma e stampa la il messaggio “stringa
#palindroma di lunghezza ”, seguito dalla lunghezza della stringa. Esempio
#• Inserendo la stringa “arcobaleno” il programma stampa “non palindroma, inserire una stringa
#palindroma: ”; inserendo successivamente “mamma’” il programma stampa “non palindroma,
#inserire una stringa palindroma”; inserendo ‘itopinonavevanonipoti’ il programma termina e
#stampa “stringa palindroma di lunghezza 21”

s=input("Inserisci una stringa e ti dirò se è palindroma o no ")
i=0
j=len(s)-1

while i<j:
    if s[i]==s[j]:
        i+=1
        j-=1
    elif s[i]!=s[j]:
        s=input("non palindroma, inserire una stringa palindroma:")
        i=0
        j=len(s)-1
print("Stringa palindroma di lunghezza",len(s))
