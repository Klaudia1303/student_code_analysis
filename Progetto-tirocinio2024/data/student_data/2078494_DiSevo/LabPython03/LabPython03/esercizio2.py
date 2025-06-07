n = int(input('Inserisci un numero maggiore di 0: '))

while n <= 0:
    print('Il numero inserito non è maggiore di 0, riprova')
    n = int(input('Inserisci un numero maggiore di 0: '))
for i in range(1,n+1):
    if n%i==0:
        print(i)
    
