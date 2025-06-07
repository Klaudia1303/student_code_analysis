n=int(input('inserisci numero primo'))
i=2
if n==2 or n==1:
    prin(n,'è un numero primo')
else:    
   while i<n:
       if n%i==0:
           print(n,'non è un numero primo')
           i=2*n
       else:
           i=i+1
   if i==n:
       print(n,'è un numero primo')
          
#numero primo è un numero divisibile solo per 1 e se stesso. tutti i numeri sono
#divisibili per 1. se n diviso a dove a diverso d an allora nn è primo
      
    
