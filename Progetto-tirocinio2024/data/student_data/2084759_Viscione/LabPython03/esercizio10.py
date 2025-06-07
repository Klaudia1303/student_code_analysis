n=int(input("Immetti un intero maggiore di 1: "))
i=2
while i<=n:
    j=2
    d=0
    while j<i and d==0:
        if i%j==0:
            d+=1
        j+=1
    if d==0:
        print(i)
        
    i+=1
