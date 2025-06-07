n=int(input('please enter a number greater than 0: '))
if n==0 or n==1:
    print('1')
elif n>0:
    factorial=1
    for i in range (1,n+1):
        factorial=factorial*i
    print(factorial)
        

    
    
    
    

    
    
