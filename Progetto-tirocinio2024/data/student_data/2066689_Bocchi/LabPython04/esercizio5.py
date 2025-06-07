n= int(input('numero: '))
l=n

if n==0 or n==1:
    print('1')
elif n>1:
    x=n
    while x>1:
        x= x-1
        n=n*(x)
    print(str(l)+str('!')+str(' =') ,n)
