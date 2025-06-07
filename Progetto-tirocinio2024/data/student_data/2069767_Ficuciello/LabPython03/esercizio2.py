n=int(input('Inserire un intero maggiore di 0:' ))
if n<1:
    print('Il numero inserito non è valido')
else:
    i=1
    while i<=n:
        if n%i==0:
             print(i)
             i+=1
print(n)

   
    

