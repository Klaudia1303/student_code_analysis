s = input("Stringa: ")
if len(s) == 0:
    print("Input non valido")
else:
    i = 0
    c = ""
    trovato = False
    while i < len(s) and not trovato:
        if ord(s[i]) > 100:
            c = s[i]
            trovato = True
        i += 1
    if trovato:
        print("Il primo carattere con codice Unicode maggiore di 100 è", c)
    else:
        print("stringa consumata e carattere non trovato")
