n=input('inserire numero(termina con \'*\') ')
somma=0
while n!='*':
    n=int(n)
    if n<0:
        somma=somma+n
    n=input('inserire numero(termina con \'*\') ')   
print(somma)
    
