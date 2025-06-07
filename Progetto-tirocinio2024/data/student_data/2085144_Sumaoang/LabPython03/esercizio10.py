n = int(input("Inserire un numero maggiore di 1:"))

i = 2

while i<n:
    d = 2
    numeroPrimo = True
    while d<i:
        if i%d==0:
            numeroPrimo = False
        d = d+1

    if numeroPrimo:
        print(i)
    i = i+1
