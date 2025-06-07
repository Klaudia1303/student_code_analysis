n = int(input("Inserisci un numero intero: "))
i = 2
primo = 0
while i <= n:
    if n % i == 0 and n != 1 and i != n:
        primo = 0
    else:
        primo = 1
    i += 1
if primo == 1:
    print("Numero primo.")
else:
    print("Numero non primo.")
