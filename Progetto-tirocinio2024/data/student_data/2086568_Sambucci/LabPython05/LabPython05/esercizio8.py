b=int(input('Inserire valore base (dispari maggiore o uguale a 3): '))
while b<3 or b%2==0:
    print('Inserimento errato!')
    b=int(input('Inserire valore base (dispari maggiore o uguale a 3): '))
n=b//2
for i in range(1,b+1,2):
    print(' '*n+'*'*i+' '*n)
    n-=1

