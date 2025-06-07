s=input('inserisci un numero intero (* per terminare): ')
n=0
while s!='*':
    c=int(s)
    s=input('inserisci un numero intero (* per terminare): ')
    if s!='*' and c>=0:
        n=n+1
    elif s=='*':
        print(n)
    
