a=int(input('inserisci intero maggiore o uguale a 0: '))
if a>=0:
    c,b=0,1
    while a!=c:
        b*=a
        a-=1
    print(b)
        
    
