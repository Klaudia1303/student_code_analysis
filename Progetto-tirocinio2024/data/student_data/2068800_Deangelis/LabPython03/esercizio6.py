s=''
while len(s)==0:
    s=input('inserire una stringa: ')
    l=len(s)
    i=0
    while i< l:
        if ord(s[i:i+1])>100:
            print('Il primo carattere con codice Unicode maggiore di 100 è ',s[i:i+1])
            i=l
        elif i==l-1:
            print('stringa consumata e carattere non trovato')
            i=l
        else:
            i=i+1