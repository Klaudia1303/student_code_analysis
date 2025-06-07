side=int(input('please enter the side lenght: '))

for i in range (side):
    for j in range (side):
        if i==0 or i==side-1 or j==0 or j==side-1 or i==j or j==side-1-i:
            print('*',end=' ')
        else:
            print(' ', end=' ')
    print()


#ho scelto di implementare uno spazio a fine print anzichè un carattere vuoto
#per rargioni di forma, così da ottenere visivamente un quadrato e non un rettangolo.
    
