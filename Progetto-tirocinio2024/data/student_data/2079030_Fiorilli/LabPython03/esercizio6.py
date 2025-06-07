s=input('inserisci una stringa composta da almeno un carattere: ')
c=0
while c<len(s):
    if ord(s[c])>100:
        print ('il primo carattere con codice Unicode maggiore di 100 è: ',s[c])
        c=len(s)
    c=c+1
    if c==len(s):
        print ('stringa consumata e carattere non trovato')
