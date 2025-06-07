s = input("Inserire una stringa valida: ")

if (len(s) > 0):
    print(s*int(len(s)))
else:
    print("ERRORE! La stringa non può essere vuota!")
