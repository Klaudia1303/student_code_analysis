s=input('Inserire  una stringa: ')
i=0
l=len(s)
while i<l:
    print((s[i:i+1]))
    if ord(s[i:i+1])>100:
        print ('Il primo carattere con codice Unicode maggiore di 100 è',s[i:i+1])
        break
    elif i==l-1:
        print('Stringa consumata e carattere non trovato')
    i=i+1
