s=input('Inserire una stringa:')
i=0
while len(s)>=i:
    x=s[i]
    i+=1
    if int(ord(x))>100:
        print('il primo carattere con codice Unicode maggiore di 100 è', x)
    else:
        print('stringa consumata e carattere non trovato')
    
