n=int(input('inserisci un numero dispari maggiore o uguale a tre: '))
i=0
k=1
while n!=1:
    n=n-2
    i+=1
for j in range(i,-1,-1):
    spazio=' '*j
    stella='*'*k
    k+=2
    print(spazio+stella)
   
