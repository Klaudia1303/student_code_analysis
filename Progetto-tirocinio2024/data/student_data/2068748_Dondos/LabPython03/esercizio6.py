s=input('Inserisci una stringa non vuota: ')
l=len(s)-1
i=0

while i<=l:
    if ord(s[i])>100:
        print('Il primo carattere con codice Unicode maggiore di 100 è', s[i])
        i=l
    elif i==l:
        print('stringa consumata e carattere non trovato')
    i+=1
