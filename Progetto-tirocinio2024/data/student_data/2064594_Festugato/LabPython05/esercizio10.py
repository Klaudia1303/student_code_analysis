lato = int(input('inserisci un numero maggiore o uguale a 2: '))
for i in range(lato):#altezza quadrato 
    for j in range(lato):#lato
        if (i==j or (i+j==(lato-1))) or ((i==0)or(j==0)) or ((i==(lato-1)) or (j==(lato-1))):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
        
