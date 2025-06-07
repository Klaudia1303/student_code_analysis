s=int(input('inserisci un numero: '))
n=int(input('inserisci un numero: '))
prodotto=0

while n!=0 and s!=0:
    if s>0 and n>0:
        n-=1
        prodotto=prodotto+s
    elif s>0 and n<0:
        n+=1
        prodotto=prodotto-s
    elif s<0 and n<0:
        n+=1
        prodotto=prodotto-s
    elif s<0 and n>0:
        n-=1
        prodotto=prodotto+s
        
print(prodotto)

