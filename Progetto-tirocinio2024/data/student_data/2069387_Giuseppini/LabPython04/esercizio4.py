i=True
c=0

while i:
    n=int(input('inserisci un numero intero (0 per terminare): '))
    if n!=0:
        if n%3==0:
            c=c+n
    else:
        i=False
print(c)
