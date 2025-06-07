#Scrivere programma che chiede in input all’utente una stringa e
#stampa a schermo la più lunga distanza tra 2 caratteri uguali contenuti
#nella stringa. Se nessun carattere si ripete allora il programma deve
#stampare “0”. Esempi:,
#• inserendo la stringa “abracadabra”, il programma stampa 10, in
#quanto la più lunga distanza è tra la prima e l’ultima “a” ed è appunto 10
#(la prima volta è in posizione 0 e l’ultima in posizione 10).
#• Inserendo la stringa “mamme”, il programma stampa 3
#Consiglio: usate il metodo rfind()

s = str(input("Inserire una stringa: "))
count=0
for i in range(len(s)):
    if s.count(s[i])>=2:
        M=0
        first_position_i = s.find(s[i])
        last_position_i = s.rfind(s[i])
        lunghezza = last_position_i-first_position_i
        if lunghezza<M:
            M = M
        elif lunghezza>M:
            M = lunghezza
        count+=1
    else:
        count=0
if count!=0:
    print(lunghezza)
else:
    print("0")

