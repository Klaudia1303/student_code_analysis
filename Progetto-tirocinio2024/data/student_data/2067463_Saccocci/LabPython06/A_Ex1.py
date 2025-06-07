n1=int(input('Inserire un intero maggiore di 0:'))
n2=int(input('Inserire il secondo intero maggiore di 0:'))
for i in range(1,n1+1):
    if n1%i==0 and n2%i!=0:
        print(i)
        
    
