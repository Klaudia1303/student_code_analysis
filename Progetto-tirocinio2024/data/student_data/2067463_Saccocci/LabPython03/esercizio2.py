n=int(input('Inserire un numero intero maggiore di zero:'))
if n>0:
    m=1
    while n>0:
        if n%m==0:
            print(m)
        m=m+1
else:
    print('Il numero',n,'non è maggiore di 0')
