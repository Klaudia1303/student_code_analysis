corretto=True
while corretto:
    x=input('inserisci una stringa palindroma: ')
    y,n=len(x),len(x)-1
    c,controllo=0,0
    if c<n and controllo==0:
        if x[n]!=x[c]:
            controllo+=1
            corretto=True
        c=c+1
        n=n-1
    if controllo==0:
        print('stringa palindroma di lunghezza',y)
        corretto=False
