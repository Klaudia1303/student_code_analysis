n1 = int (input ('Inserisci un numero maggiore di 0: '))
n2 = int (input ('Inserisci un numero maggiore di 0: '))
i = n1
while i > 0 :
    if n1%i == 0 and n2%i != 0 :
        print (i)
    i = i -1 
