n=int(input('inserire un intero    '))
i=2
p=True
while i!=n and p:
    if n%i==0:
        p=False
    i+=1
if p:
    print('numero primo')
else:
    print('numero non primo')
    
    
