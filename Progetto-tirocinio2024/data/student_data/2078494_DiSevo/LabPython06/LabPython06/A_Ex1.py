n1 = int(input('Inserisci un primo numero (>0): '))
n2 = int(input('Inserisci un secondo numero (>0): '))
i = n1

for i in range(n1,0,-1):
    if n1 % i == 0:
        if n2 % i != 0:
            print(i)
        
