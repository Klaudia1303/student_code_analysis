# Scrivere programma che chiede in input all’utente una stringa e stampa a schermo la più lunga distanza 
# tra 2 caratteri uguali contenuti nella stringa. Se nessun carattere si ripete allora il programma deve 
# stampare “0”. Esempi:,  
# • inserendo la stringa “abracadabra”, il programma stampa 10, in quanto la più lunga distanza è 
# tra la prima e l’ultima “a” ed è appunto 10 (la prima volta è in posizione 0 e l’ultima in 
# posizione 10).  
# • Inserendo la stringa “mamme”, il programma stampa 3 
# Consiglio: usate il metodo rfind()
s=input("Inserisci una stringa : ")
d=0
for i in range(len(s)):
    first=s.find(s[i])
    last=s.rfind(s[i])
    if last-first > d:
        d=last-first
print(d)