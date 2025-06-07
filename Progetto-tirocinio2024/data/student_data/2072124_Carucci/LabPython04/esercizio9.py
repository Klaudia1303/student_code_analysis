n = int(input('Inserire un numero intero maggiore di 0: '))

x = 1
y = 0
i = 0
while i<n:
    z=x+y
    x=y
    y=z
    print(z)
    i+=1
    
