n=int(input('Inserire un intero maggiore di 2: '))
while n<2:
    print('Numero inserito errato')
    n=int(input('Inserire un intero maggiore di 2: '))
i=2
while i<=n:
    r=i%2
    if r==0:
        print(i)
        i+=1
    else:
        i+=1

    
    

    
