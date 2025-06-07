n = int(input("inserisci un numero maggiore di 1:"))
while n <=1:
    n = int(input("inserisci un altro numero maggiore di 1:"))

p = 2
r = 0
while p <= n:
    i = 2
    while i <= p:
        r = p%i
        if i == p:
            print(p)
            break
        elif r == 0:
            break
        i += 1
    p += 1
