n=int(input('Inserire un intero maggiore di 0:'))
if n<=0:
    print('L\'intero inserito deve essere maggiore di 0')
else:
    x=1
    y=1
    print(x)
    print(y)
    i=2
    while i<n:
        i+=1
        somma=x+y
        x=y
        y=somma
        print(somma)
        
        
        
