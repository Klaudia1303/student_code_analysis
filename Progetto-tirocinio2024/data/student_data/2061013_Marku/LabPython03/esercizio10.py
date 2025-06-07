n=int(input('inserisci un numero intero maggiore di 1: '))
c=2
while c<=n:
    primo=True
    d=2
    while d<c:
        if c%d==0:
            primo=False
        d+=1
    if primo==True:
        print(c)
    c+=1
        
