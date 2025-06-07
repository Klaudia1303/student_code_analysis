base=int(input('Inserisci la base (numero intero dispari >=3) '))
p=base//2
for i in range(1,base+1,2):
        print(' '*p, end='')
        p-=1
        print('*'*i) 
