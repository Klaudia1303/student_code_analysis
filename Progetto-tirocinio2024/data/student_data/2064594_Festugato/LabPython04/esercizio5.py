n = int(input('inserisci un numero intero maggiore o uguale a 0: '))
i = 1
fat = n

while i>=0 and i<n:
    if n == 0 or n==1:
        print('1')
        i == -1
    else:
        fat = fat*(n-i)
        i += 1
        
        
print(fat)

