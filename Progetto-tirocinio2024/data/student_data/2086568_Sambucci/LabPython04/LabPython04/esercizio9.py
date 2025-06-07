n=int(input('Inserire un intero maggiore di 0: '))
while n<=0:
    print('Inserimento errato!!')
    n=int(input('Inserire un intero maggiore di 0: '))
i=1
j=1
sommaFib=0
print(i)
print(j)
while n>=i and n>=j:
    sommaFib=i+j
    print(sommaFib)
    j=i
    i=sommaFib
    
