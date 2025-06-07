s=input('Inserisci una stringa con almeno un carattere: ')
i=0
while (i<(len(s))) and (ord(s[i])<=100):
    i += 1
if ord(s[-1])<=100:
    print('Stringa consumata e carattere non trovato')
elif ord(s[i])>100:
    print('Il primo carattere con codice Unicode maggiore di 100 è "'+s[i]+'"')