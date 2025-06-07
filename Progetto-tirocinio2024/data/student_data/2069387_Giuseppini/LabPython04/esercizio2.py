
i=True
c=0
while i:
    n=input('inserisci un numeto intero (* per terminare): ')
    if n!='*':
        if int(n)>=0:
            c=c+1
    else:
        i=False
        
    

print(c)
