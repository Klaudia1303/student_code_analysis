finito=False
while not finito:
    s=input('inserire stringa')
    i=0
    while i<len(s) and ord(s[i])<100:
            print(s[i])
            i=i+1
    if ord(s[i])<100:
        print('stringa consumata e carattere non trovato')
    if ord(s[i])>100:
        print('Il primo carattere con codice Unicode maggiore di 100 è:',s[i])
        finito=True

       
