n = int(input('Inserisci un numero intero maggiore di 1: '))
i = 2

while i <= n:
    
    k=0
    m = 1
    
    while m <= i:
        
        if i%m == 0:

            k += 1

        m +=1

    if k == 2:

        print (i)

    i += 1
