d=int(input('Inserire dimensione (dispari maggiore o uguale a 3): '))
while d<3 or d%2==0:
    print('Inserimento errato!')
    d=int(input('Inserire dimensione (dispari maggiore o uguale a 3): '))
print()
for i in range(d):
    if i==0 or i==d-1:
        print('*'*d)
    else:
        print('*'+' '*(d-2)+'*')
