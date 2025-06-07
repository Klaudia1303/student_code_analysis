num = int(input("Inserisci un numero intero: "))

prime = True

if num > 1:
    i = 2
    while i < num:
        if num % i == 0:
            prime = False
            break
        i += 1
else:
    prime = False


if prime:
    print("numero primo")
else:
    print("numero non primo")
