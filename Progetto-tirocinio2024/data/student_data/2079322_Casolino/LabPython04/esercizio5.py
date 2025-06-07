n=0
while n>=0:
    n=int(input('Inserisci un numero intero: '))
    if n==0 or n==1:
        print('Il fattoriale di 0 o 1 è: 1')
        n=-1
    elif n!=0 and n!=1:
        p=n*n
        print('Il fattoriale del numero scelto è: ',p)
        n=-1
