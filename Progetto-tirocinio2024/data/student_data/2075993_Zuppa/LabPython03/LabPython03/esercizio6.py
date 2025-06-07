s=input('inserire una stringa non vuota   ')
while len(s)==0:
    s=input('inserire una stringa non vuota   ')
i=0
trovato=False
while not trovato and i!=len(s):
    if ord(s[i])>100:
        trovato=True
    i+=1
if trovato :
    print('il primo carattere con codice Unicode maggiore a 100 è',s[i-1])
else:
    print('stringa consumata e carattere non trovato')

