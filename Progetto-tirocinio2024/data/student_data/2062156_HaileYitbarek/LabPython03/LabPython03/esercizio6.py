a=False
while a!=True:
    s=input('inserire stringa non vuota: ')
    if s=='':
        s=input('inserire stringa non vuota: ')
    b=0
    d=0
    while b<len(s):
        c=s[b]
        b=b+1
        if ord(c)>100:
            print('Il primo carattere con codice Unicode maggiore di 100 è',c)
            a=True
        if ord(c)<100:
            d=d+1
            if d==len(s):
                print('stringa consumata e carattere non trovato')
                a=True

    
    
    

