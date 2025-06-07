n = int(input('Inserire un numero intero: '))
i = 1
c = 0
e = 0

while i < n+1:
        
    m = n%i
    if m == 0:

        c += 1

    i += 1

if c == 2:

    print('numero primo')

else:

    print('non numero primo')

    

        
