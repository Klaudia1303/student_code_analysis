corretto=False
while not corretto:
    n=int(input('inserisci numero intero n:'))
    if n%2==0 and n!=2 or n<0 or (n**0.5)+1==0:
        print('numero non primo')
        corretto=True
    else:
        print('numero primo')


        
          
