n=int(input('inserire un numero intero maggiore di 1: '))
i=2
while i!=n+1:
    j=1
    k=0
    while j!=i+1:
        if i%j==0:
            k+=1
        j+=1
    if k==2:
        print(i)
    i+=1
        