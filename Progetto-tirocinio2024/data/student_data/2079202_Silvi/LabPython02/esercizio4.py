print("questo programma verifica se il primo e l'ultimo carattere di una stringa in input siano uguali\n")
s=input("inserire la stringa:")
while len(s)==0:
    print("Errore: dati non inseriti, riprova\n")
    s=input("inserire la stringa:")
if s[0]==s[len(s)-1]:
    print("carattere iniziale e finale uguale")
else:
    print("carattere iniziale e finale diversi")
    
