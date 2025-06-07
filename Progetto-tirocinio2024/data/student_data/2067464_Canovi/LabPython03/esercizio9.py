n = input("inserisci un numero intero: ")
n = int(n)
a = 1
b = 0
while a < n:
    if n % a == 0:
        b = b + 1
    a = a + 1
    if b == 2:
        a = n
    
if b >= 2 or n == 1:
    print("numero non primo")
else:   print("numero primo")


