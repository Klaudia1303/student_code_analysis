n=int(input('inserire un numeor intero maggiore di 3: '))
c=0
i=0
for c in range(n):
    if c==0 or c==n-1:
        print('*'*n)
    else:
        print('*'+' '*(n-2)+'*')
