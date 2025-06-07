n1 = int(input('inserisci un intero positivo: '))
n2 = int(input('inserisci un intero positivo: '))
for i in range(n1 + 1, 1, -1):
    if n1 % i == 0 and n2 % i != 0:
        print(i)

    
