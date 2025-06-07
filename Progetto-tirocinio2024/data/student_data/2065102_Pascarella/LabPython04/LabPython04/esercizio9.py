n=int(input('inserisci intero'))
if n>0:
    x=1
    y=0
    c=0
    while c!=n:
        z=y
        y=x+y
        x=z
        print(y)
        c=c+1
