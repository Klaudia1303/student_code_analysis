n=int(input('inserisci un numero intero: '))
i=2
t=False
while i<n:
    if n%i==0:
        t=True
    i+=1
    
if t:
    print('non primo')
else:
    print('primo')
