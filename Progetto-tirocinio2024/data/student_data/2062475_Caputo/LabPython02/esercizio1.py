hh = input ("inserire il numero di ore: ")
mm = input ("inserire il numero di minuti: ")
ss = input ("inserire il numero di secondi: ")
hh = int (hh)
mm = int (mm)
ss = int (ss)
hhs = (hh*60)*60
mms = mm*60
tot = hhs+mms+ss
print ("il numero totale in secondi è:" , tot)
