n=int(input('scrivere un intero maggiore di 2: '))
if n>2:
    i=2
    if n%2==0:
        while i<n:
            print(n)
            n=n-2
        print(2)
    else:
        n=n-1
        while i<n:
            print(n)
            n=n-2
        print(2)
        
        
    
else:
    print('input non valido')
