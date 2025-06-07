s=input("Inserire un intero ('*' per terminare): ")
if s!='*':
    somma=0
    while s!='*':
        if int(s)>=0:
            somma+=1
            s=input('Inserire un intero ("*" per terminare):' )
        else:
            s=input('Inserire un intero ("*" per terminare):' )
    
print(somma)

