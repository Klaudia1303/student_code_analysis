n=int(input('inserisci un numero >1: '))
c=1
i=1
k=0
print (i)

while c < n:
    somma=i+k
    k= i
    i= somma
    c += 1
    print (somma)
