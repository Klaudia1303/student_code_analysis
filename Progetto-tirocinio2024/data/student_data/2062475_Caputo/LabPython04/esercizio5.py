n = int( input("inserire un numero n intero maggiore o uguale a 0, n: "))
if (n == 1 or n == 0):
    print ('1')
else:
    fattoriale = 1
    while n > 0:
        fattoriale = fattoriale * n
        n = n - 1
print ("il valore di n! è:", fattoriale)
        
