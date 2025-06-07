n=int(input('inserire intero >=3: '))
i=1
while i<=n:
    if i==1 or i==n:
        print('*'*n)
    else:
        print('*'+' '*(n-2)+'*')
    i+=1
