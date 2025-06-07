n=int(input('inserie un numero intero: '))
i=2
while (i<n and n%i!=0):
    i=i+1
if(i==n):
    print('numero primo')
else:
    print('numero non primo')
