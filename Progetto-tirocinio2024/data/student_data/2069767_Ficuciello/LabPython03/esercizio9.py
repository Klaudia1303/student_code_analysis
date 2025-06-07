n=int(input('inserire un intero positivo maggiore di 1:' ))
i=2
if n>1:
    while i<n and n%i!=0:
       i+=1
    if i==n:
        print('numero primo')
    else:
        print('numero non primo')
