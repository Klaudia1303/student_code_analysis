s=input('inserisci una stringa: ')
j=0
i=True
while i and j<len(s):
    if ord(s[j])>100:
        print('il primo carattere con codice Unicode maggiore di 100 è',s[j])
        i=False
    j=j+1
if i:
    print('stringa consumata e carattere non trovato')

