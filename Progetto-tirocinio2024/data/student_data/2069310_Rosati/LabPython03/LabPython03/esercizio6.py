s=input("Inserisci stringa: ")
i=0
boolean=True
while boolean and i<len(s):
      if ord(s[i])>100:
         boolean=False
         print("Il primo carattere con codice Unicode maggiore di 100 è",s[i])
      else:
         i+=1
if boolean:
   print("Stringa consumata e carattere non trovato")
    
