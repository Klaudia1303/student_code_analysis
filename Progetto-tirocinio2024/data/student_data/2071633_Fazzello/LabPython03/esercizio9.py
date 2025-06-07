#9) Scrivere un programma python che chiede in input all’utente un intero n e controlla se n è un numero
#primo. In caso affermativo stampa “numero primo”, altrimenti stampa “numero non primo”. Esempio:
#• Inserendo l’intero “7”, il programma stampa “numero primo”
#• Inserendo l’intero “4096”, il programma stampa “numero non primo”


n= int(input("Inserisci un numero positivo intero:"))
i=1
c=0
while i<=n:
        if n%i==0:
            c+=1
        i+=1
if c==2:
    print("\nnumero primo")
else:
    print("\nnumero non primo")
