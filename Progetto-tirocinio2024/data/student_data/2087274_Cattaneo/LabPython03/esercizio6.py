s=input('stringa=')
i=0
while i<len(s):
    if ord(s[i])>100:
        print('Il primo carattere con codice Unicode maggiore di 100 è',s[i])
        break
    else:
        print(s[i])
    i+=1
    if i>=len(s):
        print('stringa consumata e carattere non trovato')
