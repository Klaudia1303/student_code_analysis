numero_ore=int(input("Inserisci numero di ore hh: "))
numero_minuti=int(input("Inserisci numero di minuti mm: "))
numero_secondi=int(input("Inserisci numero di secondi ss: "))

hh=3600
mm=60
ss=1

tot_secondi=(numero_ore*hh)+(numero_minuti*mm)+(numero_secondi*ss)

print("Il numero di secondi equivalente e': ", tot_secondi)