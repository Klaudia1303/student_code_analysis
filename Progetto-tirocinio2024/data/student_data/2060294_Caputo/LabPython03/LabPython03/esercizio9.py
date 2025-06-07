n=input('inserisci un numero intero: ')
n=int(n)
i=2
while i<n and n%i!=0:
    i=i+1
if i==n:
     print(n, 'è numero primo')
else:  
     print(n, 'non è numero primo')
        
