#Scrivere un programma che chiede in input all’utente un numero di ore hh,numero di minuti
#mm e numero di secondi ss e stampa a video l’equivalente in numero secondi. Ad esempio, se hh = 2,
#mm = 1 e ss = 11, ilprogramma deve stampare “7271”.
h=int(input("Inserisci il numero di ore:"))
m=int(input("Inserisci il numero di minuti:"))
s=int(input("Inserisci il numero di secondi:"))
h=h*3600
m=m*60

print("Il totale in secondi è:", s+h+m)
