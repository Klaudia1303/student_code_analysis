s=input('Inserisci una stringa: ')
i=0
while i<len(s):
    if ord(s[i])<=100:
        i+=1
    else:
        print('Il primo carattere con codice Unicode maggiore di 100 è'+' '+s[i])
        i=len(s)+1
if i==len(s):
    print('stringa consumata e carattere non trovato')
