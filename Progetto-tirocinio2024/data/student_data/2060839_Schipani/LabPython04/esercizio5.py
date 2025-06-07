n=int(input('inserisci un numero maggiore o uguale a 0 '))
i=(n-1)
if n==0 or n==1:
    print('1')
elif n>1:
    while i!=0:
        n=n*i
        i-=1
    print(n)
