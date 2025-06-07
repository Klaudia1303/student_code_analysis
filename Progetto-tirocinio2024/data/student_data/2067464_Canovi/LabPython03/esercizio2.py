a = input("inserisci un numero maggiore di 0: ")
a = int(a)
b = 1
while b <= a:
    if a % b == 0:
        print(b)
    b = b + 1
