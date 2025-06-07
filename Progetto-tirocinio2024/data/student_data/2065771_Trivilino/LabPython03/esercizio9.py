n=int(input('Inserire un intero: '))
i=1
if n==1:
    print ('Numero non primo')
while i<n:
    if n%i==0  and i!=1:
        print ('Numero non primo')
        break
    elif i==n-1:
        print ('Numero primo')
        break
    i+=1
