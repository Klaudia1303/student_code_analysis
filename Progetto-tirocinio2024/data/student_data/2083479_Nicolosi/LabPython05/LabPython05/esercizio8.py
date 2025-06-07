base=int(input('Inserisci la base (un intero dispari maggiore o uguale a 3): '))
x=base//2
while x>=0:
    for i in range(1,base+1,2):
        print(' '*x+'*'*i)
        x=x-1