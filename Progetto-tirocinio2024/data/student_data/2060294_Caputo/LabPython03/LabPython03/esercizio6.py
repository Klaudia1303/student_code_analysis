s=input('inserisci una stringa con almeno 1 carattere: ')
i=0
while i<=len(s):
    print(s[i])
    i=i+1
    if int(ord(s[i]))>100 :
        print('Il primo carattere con codice Unicode maggiore di 100 è: ', s[i])
print('la stringa è terminata carattere Unicode maggiore di 100 non trovato')

