s = input("Inserire stringa: ")

if (len(s) > 0):
    if (ord(s[0]) == ord(s[len(s)-1])): #Questa condizione confronta i caratteri in base ai valori della tabella Unicode.
        print("caratteri iniziale e finale uguali")
    else:
        print("caratteri iniziale e finale diversi")
else:
    print("ERRORE! La stringa non può essere vuota.")
