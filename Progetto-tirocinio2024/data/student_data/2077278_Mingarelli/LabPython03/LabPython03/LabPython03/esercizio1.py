n=input('inserisci un mumero maggiore di 2 ')
n=int(n)
if n>=2:
    if n%2==0:
        while n>=2:     
            print(n)
            n=n-2
    else:
        n=n-1
        while n>=2:     
            print(n)
            n=n-2
else:
    print('numero sbagliato')
        
