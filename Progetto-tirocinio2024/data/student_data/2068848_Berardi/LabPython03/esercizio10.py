n = int(input("inserisci un numero intero: "))
i = 2
while i<n:
    c = True
    j=2
    while j<i:
        if i%j==0:
            c = False
        j += 1
    if c:
        print(i)
    i += 1