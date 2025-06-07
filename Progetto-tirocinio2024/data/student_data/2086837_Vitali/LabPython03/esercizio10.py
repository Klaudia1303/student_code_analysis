n=int(input("Insersici numero n maggiore di 1: "))
while n<1:
    print("Input non valido")
    n=int(input("Insersici numero n maggiore di 1: "))
i=2
f=2
while i<=n:
    f=2
    while f<=i/2:
        if i%f==0:
            break
        f +=1
    if f>i/2:
        print("\n",i)
    i +=1
     
    
    
        
