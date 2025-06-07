s=input('inserisci una stringa di caratteri: ')
x=0
while x<len(s):
    i=s[x]
    controllo=ord(i)
    if controllo<100:
        print('stringa consumata e carattere non trovato')
        x=len(s)
    elif controllo>100:
        print('il primo carattere con codice unicode maggiore di 100 è', i)
        x=len(s)
    x=x+1

