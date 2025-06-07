print("ESERCIZIO 1: inserimento di un orario (ore, minuti e secondi), \
per visualizzare il totale dei secondi\n")
hh=int(input("Inserisci le ore: \t"))
mm=int(input("Inserisci i minuti: \t"))
ss=int(input("Inserisci i secondi: \t"))
if hh<25 and hh>-1 and mm<61 and mm>-1 and ss<61 and ss>-1:
    print("I secondi totali risultano: ",(ss+(mm*60)+(hh*3600)))
else:
    print("Valori inseriti non validi")
