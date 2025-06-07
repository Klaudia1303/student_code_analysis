n=int(input('inserire un intero: '))
i=2
if n==2:
    print('il numero è primo')
else:
    while n%i!=0 and i<(n-1):
        i+=1
    if n%i==0:
        print('il numero non è primo')
    elif n%i!=0:
        print('il numero è primo')
        
    

   
    