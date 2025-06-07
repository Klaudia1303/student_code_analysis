a = input("inserisci un numero intero tra 1 e 10: ")
a = int(a)
b = input("inserisci un altro numero intero tra 1 e 10: ")
b = int(b)
n = 0

while n <= 10:
    if n != a and n != b:
        print(n)
    n = n +1
    
