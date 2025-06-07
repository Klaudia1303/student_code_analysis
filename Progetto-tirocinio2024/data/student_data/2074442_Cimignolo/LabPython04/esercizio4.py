sommaDx3=0
boo=True

while boo:
    n=int(input('inserisci un numero intero (0 per terminare): '))
    if n==0:
        boo=False
    elif n%3==0:
        sommaDx3+=n
        
print(sommaDx3)
        
        
