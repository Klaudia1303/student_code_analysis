n=int(input('n='))
i=2
while i<=n:
    j=2
    m=0
    while j<=i:
        if i%j==0:
            m+=1
        j+=1
    if m<2:
        print(i)
    i+=1
            
