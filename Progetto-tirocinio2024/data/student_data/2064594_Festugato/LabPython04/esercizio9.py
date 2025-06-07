n = int(input('inserisci un numero intero maggiore di 0: '))
i = 0
successione = 0
pre1  = 1
pre2 = 1
print(pre1)
print(pre2)


while i>=0 and i<(n-2):
    successione = pre1 + pre2
    print(successione)
    pre1 = successione-pre1
    pre2= successione
    i+=1
    
    
    
