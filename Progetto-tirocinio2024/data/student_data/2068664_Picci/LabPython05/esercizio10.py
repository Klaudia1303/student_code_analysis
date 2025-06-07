n=int(input('inserisci dimensione del lato del quadrato:'))
for i in range(0, n):
    for j in range(0, n):
        if (i == 0 or i == n - 1 or j == 0 or j == n - 1 or i == j or i == n - 1 - j):
            print( "*", end="")
        else:
            print( " ",end="")
    print("")
         
