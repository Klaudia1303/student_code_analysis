print("ESERCIZIO 3: inserimento di una stringa e di un intero, \
fa stampare la stringa solo se il numero è dispari\n")
a=int(input("Inserisci un numero intero: \t"))
s=str(input("Inserisci una stringa: \t"))
if a%2==0:
    print("Il numero non è dispari, quindi non stampo la stringa\n")
else:
    print("Il numero è dispari, quindi stampo la stringa: ",s)
