s=input('inserisci una stringa non vuota: ')
conta=0
while conta<len(s):
    if ord(s[conta])>100:
        print('il primo carattere con codice Unicode maggiore di 100 è: ',s[conta])
        break
    elif conta == len(s)-1:
        print('stringa consumata e carattere non trovato')
    conta+=1