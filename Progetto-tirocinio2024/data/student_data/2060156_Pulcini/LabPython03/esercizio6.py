finito=False
s=input('inserire una stringa:')
i=0
while not finito or i<len(s) :
    if ord(s[i])>100:
        finito=True
    i+=1
if i==len(s) and not finito:
    print('stringa consumata e carattere non trovato')
else:
    print('il primo carattere con codice Unicode maggiore di 100 è:', s[i-1])
