s=input('inserire una stringa:')
if len(s)==0:
    print('inserire una stringa composta da almeno un carattere')
    s=input('inserire una stringa:')
l=len(s)
i=0
i=int(i)
t=ord('s[i]')
while i<=l:
    if t>100:
        print('il primo carattere con codice Unicode maggiore di 100 è:',s[i])
    i+=1
print('stringa consumata e carattere non trovato')

