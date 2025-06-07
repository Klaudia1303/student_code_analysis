s = str(input("Inserisci una stringa con almeno un carattere: "))
while s == "":
    s = str(input("Input non valido. Inserisci una stringa con almeno un carattere: "))
i = 0
while i < len(s) and ord(s[i]) <= 100:
    if ord(s[(i+1)]) > 100:
        print("Il primo carattere con codice Unicode maggiore di 100 è", s[(i+1)])
    if i == (len(s) - 1):
        print("Stringa consumata e carattere non trovato.")
    i += 1
