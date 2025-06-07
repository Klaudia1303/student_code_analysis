s=input('inserisci una stringa: ')
l=len(s)

a=0
while a<=1:
    if ord(s[a])>100:
        print('Il primo carattere con codice Unicode maggiore di 100 è ', s[a])
    elif a==1:
        print('stringa consumata e carattere non trovato')
    a+=1
