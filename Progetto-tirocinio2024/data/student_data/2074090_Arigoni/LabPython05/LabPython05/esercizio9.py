n=int(input('Lato quadrato '))
for i in range(n):
    if i==0 or i==n-1:
        print('*'*n)
    elif i==1 and n==3:
        print('* *')
    else:
        print('*',' '*int(n-4),'*')
