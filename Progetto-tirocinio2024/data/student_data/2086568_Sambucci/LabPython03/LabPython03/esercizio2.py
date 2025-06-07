n=int(input('Inserie un numero intero maggiore di zero: '))
while n<0:
    print('Numero inserito errato')
    n=int(input('Inserire un intero maggiore di 0: '))
i=1
while i<=n:
    r=n%i
    if r==0:
        print(i)
        i+=1
    else:
        i+=1
