n=int(input('scrivere un numero intero maggiore di 0: '))
if n>=3:
    i=3
    x=1
    y=1
    z=2
    print(x)
    print(y)
    print(z)
    while i<n:
        x=y
        y=z
        z=y+x
        print(z)
        i=i+1
else:
    if n==1:
        print('1')
    elif n==2:
        print('1')
        print('1')
    else:
        print('input non valido')

    
