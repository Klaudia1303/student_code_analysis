n=int(input('inserire un numero intero maggiore di 1   '))
while n<2:
    n=int(input('inserire un numero intero maggiore fi 1   '))
i=2
while i!=n:
    p=True
    k=2
    while p and k!=i:
        if i%k==0:
            p=False
        k+=1
    if p:
        print(i)
    i+=1
