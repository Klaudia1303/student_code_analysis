n=int(input("immettere numero intero positivo maggiore di 1: "))
i=2
while i<=n:
    j=1
    check=True
    while j<i:
        if j!=1 and j!=i:
            if i%j==0:
                check=False
        j+=1
    if check:
        print(i)
    i+=1


