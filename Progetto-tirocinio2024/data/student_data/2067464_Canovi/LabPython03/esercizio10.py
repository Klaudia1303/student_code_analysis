n = input("inserisci un numero maggiore di 1: ")
n = int (n)
n1 = 2
while n1 <= n:
    div = 1
    numDiv = 0
    while div < n1:
        if n1 % div == 0:
            numDiv = numDiv + 1
        div = div + 1         
        if numDiv == 2:
            div = n1
    if numDiv < 2:
        print(n1)
    n1 = n1 + 1






