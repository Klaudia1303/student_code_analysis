n1=int(input('Inserire primo numero intero: '))

while n1<0:
    print('Inserimento primo numero errato!')
    n1=int(input('Inserire primo numero intero: '))

n2=int(input('Inserire secondo numero intero: '))

while n2<0:
    print('Inserimento secondo numero errato!')
    n2=int(input('Inserire secondo numero intero: '))
    
for i in range(n1,n2):
    if i%n1==0:
        print(i)
