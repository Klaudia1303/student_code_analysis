n=int(input('Inserisci un numero intero:'))
div=2
c=0
while div<=n/2 and c==0:
    if n%div==0:
        c+=1
    div+=1
if c==0:
    print('numero primo')
else:
    print('numero non primo')
    
