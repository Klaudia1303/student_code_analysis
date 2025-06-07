s=input('inserisci una stringa ')
if len(s)>=1:
    while len(s)!=0:
        if ord(s[0])<=100 and s!='*':
            s=s[1:len(s)]
        elif ord(s[0])>100:
            print('Il primo carattere con codice Unicode maggiore di 100 è ',s[0])
            s='*'
if s!='*':
    print('stringa consumata e carattere non trovato')
