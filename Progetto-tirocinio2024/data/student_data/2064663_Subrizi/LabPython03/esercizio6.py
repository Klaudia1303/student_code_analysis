s = input('Inserisci una stringa lunga almeno un carattere: ')
lung = 0
c=0
while lung<len(s):
    if ord(s[c])<100:
        print(s[c])
        lung += 1
        c += 1
        if lung==len(s):
            print('stringa consumata e carattere non trovato')
    else:
        print('Il primo carattere con codice Unicode maggiore di 100 è',s[c])
        lung=len(s)
