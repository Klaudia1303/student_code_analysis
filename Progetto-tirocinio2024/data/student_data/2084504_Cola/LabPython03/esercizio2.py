n=int(input('scrivere un numero intero maggiore di zero: '))
if n>0:
    i=1
    while i<=n:
        if n%i==0:
            print(i)
        i=i+1
else:
    print('input non valido')
