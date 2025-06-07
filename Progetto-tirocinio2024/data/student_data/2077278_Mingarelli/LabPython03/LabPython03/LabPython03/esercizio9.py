n=int(input('inserisci un numero intero'))
c=0
i=1
while i<=n:
    if n%i==0:
       c+=1
    i+=1
if c==2:
    print('numero primo')
else:
    print('numero non primo')
    
   
