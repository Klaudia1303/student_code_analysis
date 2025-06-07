s = input('inserisci una stringa: ')
i = 0
b = True
while i<=len(s)-1 and b:
    if ord(s[i])>100:
        print('Trovato carattere Unicode maggiore di 100: ' + s[i])
        b = False
    else:
        i += 1
    if i > len(s) and b:
        print('stringa consumata e carattere non trovato: ')
        b = False
        
