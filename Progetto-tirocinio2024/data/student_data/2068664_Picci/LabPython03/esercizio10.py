k=int(input('inserisci numero n>1:'))
if k==2:
    print(2)
elif k==3:
    print(2)
    print(3)
else:
    n=int(3)
    while n<=k:
        i=int(2)
        while n%i!=0 and i<n/2:
            i+=1
        if n%i!=0:
            print(n)
        n+=1
