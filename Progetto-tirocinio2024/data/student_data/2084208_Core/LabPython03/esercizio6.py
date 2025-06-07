s=input('Inserire una stringa composta almeno da un carattere: ')
i=0
while i<len(s) and ord(s[i])<=100:
    print(s[i])
    i+=1
if i>=len(s):
    print('stringa consumata e carattere non trovato')
else:
    print('Il primo carattere con codice Unicode maggiore di 100 è',s[i])
