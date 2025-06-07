n=int(input("Inserire un numero intero positivo (maggiore di 1): "))
c=1
i=2
while c!=n:
    c+=1
    if c%i==0:
        if c==i:
            print(i)
            i=2
    else:
        i+=1
        c-=1
    
