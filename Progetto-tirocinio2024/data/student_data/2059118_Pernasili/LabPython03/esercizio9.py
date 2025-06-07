n = int(input("Inserisci un numero intero positivo maggiore di 1: "))
i = 2
c = 0
while i<= n:
    if n % i == 0:
        i = i+1
        c = c+1
    else:
        i= i+1
if c > 1:
    print("numero non primo")
else:
    print("numero primo")
