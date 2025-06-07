n=int(input('Inserire numero intero maggiore di 1: '))
i=2
while i<=n:
    j=2
    corretto=True
    while j<i:
        if i%j==0:
            corretto=False
        j+=1
    if corretto:
        print(i)
    i+=1
            
