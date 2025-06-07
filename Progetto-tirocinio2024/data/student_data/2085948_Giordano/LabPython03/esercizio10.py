n=int(input("Inserisci un numero maggiore di 1: "))
for i in range(2,n):
    if (n % i) == 0:
        print(i-1)
        break
    else:
        print(i)
        break 