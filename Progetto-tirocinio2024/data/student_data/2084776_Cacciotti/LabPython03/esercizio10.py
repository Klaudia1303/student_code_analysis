n = int(input('inserire valore intero positivo maggiore di 1'))
i = 2
int (i)
while i<=n:
    k = 1
    int (k)
    somma = 0
    while k <= i:
        if (i%k == 0):
            somma = somma + 1
        k += 1
    if (somma==2):
        print (i)
    i +=1
