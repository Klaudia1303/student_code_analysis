n = int(input ("inserire un numero intero positivo maggiore di 1: "))
i = 2
int (i)
while i <= n:
    j = 1
    int (j)
    somma = 0
    while j <= i:
        if (i%j == 0):
            somma = somma + 1
        j += 1
    if (somma == 2):
        print(i)
    i += 1
