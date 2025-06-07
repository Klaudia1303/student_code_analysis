n = int(input('Inserire un numero intero: '))
if n > 0:
    n1 = n2 = 1 #perchè i primi due numeri della successione sono 1 e 1
    i = 2
    if n == 1:
        print(n1)
    elif n > 1:
        print(n1, n2, sep = '\n')
    while i < n:

        #dopo aver controllato che n > 1, devo stampare,
        #oltre a 1 1, gli altri numeri della successione fino a n
    
        n3 = n1 + n2
        n1 = n2
        n2 = n3

        #ogni numero è dsto dalla somma dei precedenti
    
        print(n3)
        i += 1

        #incrremento di 1 il contatore per analizzare tutti i numeri fino a n

else:
    print('Intero minore di 0')

