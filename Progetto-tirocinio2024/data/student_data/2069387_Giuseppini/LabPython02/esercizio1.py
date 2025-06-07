#Scrivere un programma che chiede in input all’utente un numero di ore hh, numero di minuti mm e numero di
#secondi ss e stampa a video l’equivalente in numero secondi. Ad esempio, se hh = 2, mm = 1 e ss = 11, il
#programma deve stampare “7271”.

hh=int(input('scrivi le ore: '))
mm=int(input('scrivi i minuti: '))
ss=int(input('scrivi i secondi: '))

print((hh*60*60)+(mm*60)+ss)
