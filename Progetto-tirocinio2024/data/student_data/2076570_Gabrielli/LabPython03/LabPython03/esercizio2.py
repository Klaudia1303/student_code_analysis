n=int(input('inserire numero intero maggiore di 0: '))

if n<1:
    print('numero inserito non valido')
else:
    i=1
    while i<=n:
        if n%i==0:
            print('i suoi divisori: ')
        i+=1
