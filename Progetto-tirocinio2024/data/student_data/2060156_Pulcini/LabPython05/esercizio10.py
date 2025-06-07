lato=int(input('inserire lunghezza lato:'))
for i in range(lato):
    for j in range(lato):
        if i==0 or i==lato-1:
            print('*', end='')
        elif j==0 or j==lato-1:
            print('*', end='')
        elif j==i or j==lato-1-i:
            print('*', end='')
        else:
            print(' ', end='')
    print()
