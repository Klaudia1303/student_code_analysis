
n1=int(input("Inserire intero positivo:\t"))
n2=int(input("Inserire intero positivo:\t"))

for i in range(n1,1,-1):
    if n1%i==0:
        if n2%i!=0:
            print(i)
        
