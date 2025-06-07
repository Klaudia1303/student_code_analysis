n=int(input('inserire un numero maggiore di 1: '))
a=2
b=0
while a<=n:
    if n%a==0:
        a=a+1
        b=b+1
    else:
        a=a+1
if b>1:
    print('numero non primo')
else:
    print('numero primo')
       
    
        
        
        
    
    
