x=int(input('inserisci n: '))
if x<=1:
    print('numero maggiore di uno')
else:
    div,controllo=2,0
    while div<=x/2 and controllo==0:
        if x%div==0:
            controllo+=1
        div+=1
    if controllo==0:
        print('primo')
    else:
        print('non primo')
    
