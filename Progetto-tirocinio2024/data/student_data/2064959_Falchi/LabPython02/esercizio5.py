anno_str = input("Inserisci l'anno: ")

if len(anno_str) == 4: #Controlla se il valore inserito è vuoto o lungo più/meno di 4 caratteri.
    anno = int(anno_str)
    
    if ((anno % 4 == 0) and not (anno % 100 == 0)) or (anno % 4 == 0):
        print("anno bisestile")
    else:
        print("anno non bisestile")
else:
    print("ERRORE! Il valore inserito è vuoto o non valido.")
