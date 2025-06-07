c=True
while c:
    n=int(input('Intero maggiore di 2 '))
    if n>2:
        c=False
    else:
        print('Input non valido ')
while n>=2:
    if n%2!=0:
        n=n-1
    print(str(n))
    n=n-2
