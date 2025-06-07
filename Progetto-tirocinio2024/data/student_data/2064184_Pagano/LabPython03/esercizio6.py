phrase = input("Inserisci una stringa: ")

i = 0
success = False
while i < len(phrase):
    if ord(phrase[i]) > 100:
        success = True
        print("Il primo carattere con codice Unicode maggiore di 100 è " + phrase[i])
        break
    i += 1

if not success:
    print("stringa consumata e carattere non trovato")
