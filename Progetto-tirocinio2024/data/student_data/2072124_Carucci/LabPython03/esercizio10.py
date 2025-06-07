n = int(input('Inserire un numero intero maggiore di 1: '))
i = 2
while i<=n:
    primo = True
    j = 2
    while j<i and primo:
        if (i%j)!=0:
            j+=1
        else:
            primo = False
    if primo:
        print(i)
    i+=1
    
