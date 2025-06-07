hh = int(input("inserisci il numero di ore: "))
mm = int(input("inserisci il numero di minuti: "))
ss = int(input("inserisci il numero di secondi: "))

mm = mm + (hh * 60)
ss = ss + (mm*60)
print(ss)
