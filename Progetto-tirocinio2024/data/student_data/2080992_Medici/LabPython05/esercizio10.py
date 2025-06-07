lato=int(input('inserire il lato del quadrato: '))
if lato>=2:
    for i in range(lato):
        for j in range(lato):
            if i==j or lato-i-1==j or i==0 or i==lato-1 or j==0 or j==lato-1:
                print('*', end='')
            else:
                print(' ', end='')
        print('')
else:
    print('inserire un numero dispari maggiore o uguale a tre, riavviare il programma')
