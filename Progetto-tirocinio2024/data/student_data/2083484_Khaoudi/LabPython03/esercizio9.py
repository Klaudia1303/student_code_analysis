#Scrivere un programma python che chiede in input all’utente un intero n e controlla se n è un numero
#primo. In caso affermativo stampa “numero primo”, altrimenti stampa “numero non primo”. Esempio:
#• Inserendo l’intero “7”, il programma stampa “numero primo”
#• Inserendo l’intero “4096”, il programma stampa “numero non primo”
n=int(input("Inserisci un numero : "))
i=2
bo=True
while i<=n and bo==True:
    if n==i:
        print("numero primo")
    elif n%i==0:
        bo=False
        print ("numero non primo")
    
    i+=1
