s=input('scrivi un carattere: ')
l=len(s)
i=0
if l!=0:
    while i<=l-1:
        s[1]
        if ord(s[i])>100:
            print('l primo carattere con codice Unicode maggiore di 100 è: ', s[i])
        elif i==l-1:
            print('stringa consumata e carattere non trovato')
        i+=1
