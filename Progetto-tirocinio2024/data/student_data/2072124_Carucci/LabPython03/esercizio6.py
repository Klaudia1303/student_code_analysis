s = input('Inserire una stringa che contenga almeno un carattere: ')
i = 0
trovato = False
while (not trovato) and (i<len(s)):
    if ord(s[i])>100:
        trovato = True
    else:
        i+=1
if trovato:
    print('Il primo carattere con codice UNICODE maggiore di 100 è', s[i])
else:
    print('Stringa consumata e carattere non trovato')
