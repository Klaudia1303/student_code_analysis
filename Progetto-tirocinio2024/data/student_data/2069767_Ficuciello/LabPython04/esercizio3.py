n=input('Inserire intero:' )
somma=0
while n!='*' and int(n)<0:
    somma=somma+int(n)
    n=input('Inserire intero:')
    if n!='*' and int(n)>=0:
        n=input('Inserire intero:')
print(somma)
        
    
