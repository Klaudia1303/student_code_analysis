n=int(input('Inserisci un numero intero positivo maggiore di 1: '))
i=2
count=0

while i<=(n/2) and count==0:
    if n%i==0:
        count+=1
    i+=1
if count==0:
    print('numero primo')
else:
    print('numero non primo')
    
