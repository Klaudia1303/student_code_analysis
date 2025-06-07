s=input('inserisci una stringa: ')
g=0
T=False
while g<len(s) and not T:
    if ord(s[g])>100:
        print('Il primo carattere con codice Unicode maggiore di 100 è',s[g])
        T=True
    g+=1
if not T:
    print('stringa consumata e carattere non trovato')
   
