alpha = False
while not alpha:
    s = input("Inserire una stringa: ")
    if s.isalpha():
        alpha = True
i = 0
uni = False
while i < len(s) and not uni:
    if ord(s[i]) > 100:
        print("Il primo carattere con codice Unicode maggiore di 100 è "+s[i])
        uni = True
    i += 1
if uni == False:
    print("Stringa consumata e carattere non trovato")
