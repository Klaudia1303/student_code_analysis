n=int(input('inserire intero maggiore di 0: '))
k=1
i=1
for a in range(1,n+1):
    j=k+i
    k=i
    i=j
    print(j)
    