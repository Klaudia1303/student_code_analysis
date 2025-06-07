n=input('inserisci un numero maggiore di 1: ')
n=int(n)
i=2
while i<=n:
    k=1
    k=k+1
    while k<i and i%k!=0:
        k=k+1
    if k==i:
        print(i)
    i=i+1
        
