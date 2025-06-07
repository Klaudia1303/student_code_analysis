n1 = int(input('Inserire un numero : '))
n2 = int(input('Inserire un secondo numero : '))

index = 1
prodotto = 0
while(prodotto < n2):

    prodotto = n1 * index
    if((n1 * index) < n2):
        print(prodotto)
    index += 1
        
