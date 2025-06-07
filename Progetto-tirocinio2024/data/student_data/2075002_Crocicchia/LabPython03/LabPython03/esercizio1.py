n=input('inserire un numero maggiore di 2: ')
n=int(n)
conta=0
if n>2:
    while conta<n-1:
        print('\n',2+conta)
        conta+=2
else:
    print('valore non acconsentito')