num = int(input("Inserisci un intero maggiore di zero: "))

if num > 0:
    i = 1
    while i <= num:
        if num % i == 0:
            print(i)
        i += 1
