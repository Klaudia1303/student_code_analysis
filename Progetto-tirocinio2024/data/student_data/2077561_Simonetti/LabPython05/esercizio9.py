side=int(input('please enter a number: '))
for i in range(side):
    for j in range(side):
        if (i==0 or i==side-1 or j==0 or j==side-1):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
#ho scelto di aggiungere uno spazio al posto di un carattere vuoto a fine print
#per avere in output visivamente un quadrato e non un rettangolo.
