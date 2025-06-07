d=int(input('Inserire dimensione lato quadrato (maggiore o uguale a 2): '))
while d<2:
    print('Inserimento errato!')
    d=int(input('Inserire dimensione lato quadrato (maggiore o uguale a 2): '))

for i in range(d):
    for j in range(d):
        if i==0 or i==d-1:
            print('*', end='')
        elif j==0 or j==d-1:
            print('*', end='')
        elif j==i or j==d-1-i: 
            print('*', end='')
        else:
            print(' ', end='')
    print()
