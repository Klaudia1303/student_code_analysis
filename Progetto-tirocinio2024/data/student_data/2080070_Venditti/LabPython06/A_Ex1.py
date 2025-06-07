n1 = int(input('Inserisci un intero maggiore di zero: '))
n2 = int(input('Inserisci un intero maggiore di zero: '))

for i in range (max(n1,n2),0,-1):
    if n1 % i == 0 and not n2 % i == 0:
        print(i)
    
