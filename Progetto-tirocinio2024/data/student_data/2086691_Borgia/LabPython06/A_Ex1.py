n1=int(input('Inserire un numero intero maggiore di zero: '))
n2=int(input('Inserire un numero intero maggiore di zero: '))
for i in range(n1,1,-1):
    if n1%i==0:
        if n2%i!=0 or n2/i<0:
            print(i)
            
