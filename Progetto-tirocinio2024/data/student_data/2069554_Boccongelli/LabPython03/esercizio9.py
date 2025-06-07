n = int(input('Inserisci un numero intero: '))

k = 2
primo = True
while (k < n):
    if (n % k == 0):
        primo = False
    k += 1
if (primo and n != 1):
    print('numero primo')
else:
    print('numero non primo')
