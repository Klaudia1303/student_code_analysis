somma=0
check=True
n=input('inserire numero intero: ')
if n!='*':
    while check and n!='*':
        m=int(n)
        if m<0:
            somma=somma+m
            n=input('inserire numero intero: ')
        if m>0:
            n=input('inserire numero intero: ')
        elif n=='*':
            check=False
print(somma)
    
        

    
