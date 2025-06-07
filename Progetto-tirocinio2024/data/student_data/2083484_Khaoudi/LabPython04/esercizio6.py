#Scrivere un programma python che chiede in input all’utente due numeri interi e ne stampa il loro
#prodotto calcolato senza usare l’operatore * (moltiplicazione) o / (divisione).
#Esempio:
#• Inserendo l’intero “5” seguito dall’intero “2” il programma stampa “10”
#• Inserendo l’intero “-3” seguito dall’intero “4” il programma stampa “-12”
#Nota: Gli interi in input al programma possono essere positivi, negativi o pari a 0.
n1= int(input("inserisci un numero intero : "))
n2= int(input("inserisci un numero intero : "))

i=1
som=0
while i<=n2:
    som+=n1
    i+=1
    
print(som)
