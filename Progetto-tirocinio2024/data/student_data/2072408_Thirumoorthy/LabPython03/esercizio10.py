n=int(input('inserisci un intero maggiore di 1'))
a=2
if n==2:
    print(2)
elif n==3:
    print(2)
    print(3)
else:
    a=int(3)
    while a<=n:
        i=int(2)
        while a%i!=0 and i<a/2:
            i +=1
        if a%i!=0:
            print(a)
        a+=1
    
    
    
