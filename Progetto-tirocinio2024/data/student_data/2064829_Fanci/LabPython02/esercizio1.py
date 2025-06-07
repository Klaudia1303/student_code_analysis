hh = input("inserisci l'ora: ")
hh = int(hh)
mm = input("inserisci i minuti: ")
mm = int(mm)
ss = input("inserisci i secondi: ")
ss = int(ss)
print("L'ora da te indicata è: " ,hh,":",mm,":",ss)
hs = hh*3600
ms = mm*60
print("L'equivalente dell'orario in secondi è: ",ss+ms+hs)
