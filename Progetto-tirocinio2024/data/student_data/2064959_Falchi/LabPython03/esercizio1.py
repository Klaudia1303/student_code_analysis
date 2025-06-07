n = input("Inserire un intero maggiore di 2: ")

i = 1

if n.isdecimal():
    while (i <= int(n)):
        if int(i) % 2 == 0:
            print(i)
        i = i + 1
else:
    print("Errore! Valore inserito non valido.")
