n1 = int(input('Inserisci un numero maggiore di 0: '))
n2 = int(input('Inserisci un numero maggiore di 0: '))

for k in range(n1, 0, -1):
    if (n1%k==0) and (n2%k!=0):
        print(k)

        
