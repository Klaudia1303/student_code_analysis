s = input('> ')
i = 0
while i<len(s):
    if ord(s[i]) > 100:
        print('Il primo carattere con codice Unicode maggiore di 100 è', s[i])
        break
    i += 1
else:
    print('stringa consumata e carattere non trovato')
