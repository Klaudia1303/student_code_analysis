n=int(input("Inserire un intero maggiore o uguale a zero:"))
numero=1
j=n
b=True
if n==0 or n==1:
    print(1)
else:
    while b:
        numero=numero*j
        j=j-1
        if j==0:
            b=False
            print(numero)    
    
    
