a = int(input('inserisci un intero maggiore di 1: '))
i = 2
while i<=a:
    b = True
    c = 2
    while c < i:
        if i % c == 0:
            b = False
        c += 1
    if b == True:
        print(i)
    i +=1

       

