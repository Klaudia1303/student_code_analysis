Inserimento = input("Inserire un intero maggiore di 0: ")
i = 1

if Inserimento.isdecimal():
    while i <= int(Inserimento):
        if int(Inserimento) % i == 0:
            print(i)
        i = i + 1
