s=input('inserisci una stringa di almeno un carattere:')
i=0
x=ord(s[i])
f=False
while not f and i<len(s):
    x=ord(s[i])
    if x>100:
        print('il primo carattere con codice Unicode maggiore di 100 è:',s[i])
        f=True
    elif i==(len(s)-1):
        print('stringa consumata e carattere non trovato')
    i+=1


 
