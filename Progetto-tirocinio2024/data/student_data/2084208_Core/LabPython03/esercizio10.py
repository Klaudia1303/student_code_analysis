n=int(input('Inserire un numero maggiore di 1: '))
i=2
while i<=n:
    m=1
    c=0
    while m<=i:
        if i%m==0:
            c=c+1
        m+=1
    if c==2:
        print(i)
    i+=1
        
    
