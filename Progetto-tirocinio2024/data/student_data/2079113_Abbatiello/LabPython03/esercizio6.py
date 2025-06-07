s = input('inserisci stringa :')
while s == '':
    s = input('inserisci nuova stringa :')

l = len(s) - 1
i = 0

while i <= 1:
    if ord(s[i]) > 100 :
        print('il primo carattere con codice Unicode maggiote di 100 è', s[1], '')
        break
    elif i == 1:
        print('stringa consumata e carattere non trovato')
    i += 1
