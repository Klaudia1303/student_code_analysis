y=int(input('inserisci un numero intero positivo maggiore di 1: '))
x=2
if y>1:
    while not y<x:
        if x>1:
            div,controllo=2,0
            while div<=x/2 and controllo==0:
                if x%div==0:
                    controllo+=1
                div+=1
            if controllo==0:
                print(x)
        x+=1
else:
    print('numero maggiore di uno')

    

    

    
        


