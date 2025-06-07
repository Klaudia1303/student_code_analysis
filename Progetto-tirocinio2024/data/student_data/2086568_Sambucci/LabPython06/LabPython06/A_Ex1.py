n1=int(input('Inserire primo numero intero: '))
n2=int(input('Inserire secondo numero intero: '))
while n1<0:
    print('Primo numero errato!')
    n1=int(input('Inserire primo numero intero: '))
while n2<0:
    print('Secondo numero errato!')
    n2=int(input('Inserire secondo numero intero: '))
i=n1
while i>0:
    if n1%i == 0:
        if n2%i !=0:
            print(i)
    i-=1
    
    
