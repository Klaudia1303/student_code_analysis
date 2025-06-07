#Scrivere un programma che chiede in input all’utente un numero di ore hh, numero di minuti mm e numero di
#secondi ss e stampa a video l’equivalente in numero secondi. Ad esempio, se hh = 2, mm = 1 e ss = 11, il
#programma deve stampare “7271”.
hh = int(input("inserisci un ora qualsiasi :") )
mm = int(input("inserisci un numero qualsiasi che quantifica i minuti scelti :") )
ss = int(input("inserisci un numero qualsiasi che quantifica i secondi :") )
print (int(hh*3600+mm*60+ss) )
