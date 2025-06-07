n=int(input('Inserire un intero positivo maggiore di 1:'))
i=2
if n>1:
    while n>=i:
        k=1
        k+=1
        while k<i and i%k!=0:
            k+=1
        if k==i:
            print(i)
        i+=1
        

