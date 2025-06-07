print("ESERCIZIO 4: verifica che il primo carattere e l\'ultimo di una stringa\
inserita in input siano uguali o meno\n")
s=str(input("Inserire una stringa per verificare che\
il primo carattere è uguale all\'ultimo: \t"))
if len(s)!=0:
    if s[0]==s[len(s)-1]:
        print("Caratteri iniziale e finale uguali")
    else:
        print("Caratteri iniziale e finale diversi")
