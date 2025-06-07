n=int(input('inserisci numero intero:'))
i=1
div=0
while i<=n:
    if n%i==0:
       div+=1
    i+=1
if div==2:
    print('il numero è primo')
else:
    print(n,'non è un numero primo') 
