hh = input("Inserisci il numero di ore: ")
hh = int(hh)
mm = input("Inserisci il numero d minuti: ")
mm = int(mm)
ss = input("Inserisci il numero di secondi: ")
ss = int(ss)
somma = (mm * 60) + (hh * 3600) + ss
print("Il numero di secondi è: ", somma)
