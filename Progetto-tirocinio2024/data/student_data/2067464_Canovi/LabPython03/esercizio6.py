s = input("inserisci una stringa: ")
a = 0
while a < len(s):
    print(s[a])
    if ord(s[a]) > 100:
        print("Il primo carattere con codice Unicode maggiore di 100 è " + s[a])
        a = len(s)
    else:   a = a + 1
    if a == (len(s) -1) and ord(s[a]) <= 100:
        print("stringa consumata e carattere non trovato")
        a = a + 1
