i = int(input('Inserisci primo intero: '))
j = int(input('Inserisci secondo intero: '))
a = abs(j)
n = 0
while a > 0:
    n = n + abs(i)
    a -= 1
    
if (i < 0 and j > 0) or (i > 0 and j < 0) :
    n = -n

print(n)
    
