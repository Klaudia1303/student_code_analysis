n1 = int(input('Inserisci un intero: '))
n2 = int(input('Inserisci un intero: '))

p = 0
i = 0
while i < abs(n2):
    p += n1
    i += 1
if (n2 < 0):
    p = -p
print(p)
    
