n = int (input('Inserisci il lato del quadrato: '))
for i in range (n):
    for j in range (n):
        if i == 0 or i == n-1:
            print ('*', end = '')
        elif j == 0 or j == n-1:
            print ('*', end = '')
        elif i == j or i == n-j-1:
            print ('*', end = '')
        else :
            print (' ', end = '')
    print('')
