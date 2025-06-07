n = int(input("Inserire numero maggiore di 0: "))

i = 0

Prec = 1
Succ = 1
        
if n > 0:
    while i < n:
        print(Prec)
        somma = (Prec + Succ)
        Prec = Succ
        Succ = somma
        i += 1
else:
    print("ERRORE! Il numero deve essere maggiore di 0.")
