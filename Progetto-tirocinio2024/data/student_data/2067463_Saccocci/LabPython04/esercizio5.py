n=int(input('Inserire un intero maggiore o uguale di 0:'))
if n<0:
    print('L\'intero inserito non è maggiore o uguale di 0')
else:
    if n==0:
        print(1)
    elif n==1:
        print(1)
    elif n>1:
        i=1
        prod=1
        while i!=n:
            i+=1
            prod=prod*i
        print(prod)
        
    
