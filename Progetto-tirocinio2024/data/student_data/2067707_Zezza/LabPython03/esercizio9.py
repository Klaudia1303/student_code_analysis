n=int(input('numero:' ))
i=int(2)
if n==2:
    print('numero primo')
else:
    while n%i!=0 and i<n/2:
        i+=1
    if n%i==0:
        print('numero non primo')
    else:
        print('numero primo')
