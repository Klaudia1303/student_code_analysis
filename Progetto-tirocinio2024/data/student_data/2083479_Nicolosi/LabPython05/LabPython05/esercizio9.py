l=int(input('Inserisci il lato(dispari maggiore o uguale 3): '))
for j in range(1,l+1):
    print('*',end='')
print()
for i in range(l-2):
    print('*'+' '*(l-2)+'*')
for n in range(1,l+1):
    print('*',end='')