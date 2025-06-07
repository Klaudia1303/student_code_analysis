num = int(input("Inserisci un intero n>2: "))

if num > 2:
    i = 1
    while i*2 < num:
        print(i*2)
        i += 1
