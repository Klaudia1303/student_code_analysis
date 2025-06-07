n=int(input('Inserire intero: '))
corretto=True
i=2
while i<n:
    if n%i==0:
        corretto=False
    i+=1
if corretto:
    print('numero primo')
else:
    print('numero non primo')
    
