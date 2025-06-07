n=int(input('inserire un numero intero positivo maggiore di 1: '))
if n>1:
    i=2
    a=2
    while i<=n:
        if i%a==0 and i!=a:
            a=1
            i=i+1
        else:
            if a>i:
                print(i)
                a=1
                i=i+1
        a=a+1
else:
    print('input non valido')
