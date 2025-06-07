n = int(input('Inserisci un numero intero maggiore di 1: '))
cont = 2
while cont <= n:
    primo = True
    divisore = 2
    while divisore < cont:
        if cont % divisore == 0:
            primo = False
        divisore = divisore+1
    if primo == True:
        print (cont)
    cont = cont+1
