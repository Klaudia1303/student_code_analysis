n = int(input("inserisci un numero intero: "))
i = 2
while i<n:
    if n%i==0:
        print("numero non primo")
        exit()
    i += 1
print("numero primo")