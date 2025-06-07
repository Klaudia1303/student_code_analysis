n = int (input ('Inserisci un numero intero maggiore di 1: '))
i = 2
controllo = 1
while i <= n :
    #controllo numero primo
    j = 2
    while j < i:
        resto = i % j
        if resto == 0 :
            #numero non primo
            j = i + 1 
            controllo = 0
        else :
            j= j+1
            controllo = 1
    if controllo == 1:
        print (i)
    i = i+1
