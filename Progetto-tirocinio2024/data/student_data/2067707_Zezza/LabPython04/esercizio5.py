n=int(input('inserisci intero: '))
i=n-1
if n==0 or n==1:
    print('1')
elif n>1:
    while i!=0:
        n=n*i
        i=i-1
    print(n)
        
        
