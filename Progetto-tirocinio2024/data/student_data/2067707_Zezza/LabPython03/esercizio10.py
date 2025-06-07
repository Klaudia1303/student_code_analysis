k=int(input('inserisci numero: '))
n=int(3)
while n<=k:
    i=int(2)
    while n%i!=0 and i<n/2:
        i+=1
    if n%i!=0:
        print(n) 
    n+=1
