k = int(input("Inserisci un numero intero positivo n maggiore di 1: "))

if k == 2:
    print(2)
elif k ==3:
    print(2)
    print(3)
else:
    n=int(2)
    while n<= k:
        i = int(2)
        while n % i != 0 and i< n/2:
            i = i+1
        if n % i != 0 or n == 2:
            print(n)
        n = n+1
