n=input('inserire un numero maggiore di 0: ')
n=int(n)
conta=1
if n>0:
    while conta<=n:
        if n%conta==0:
            print('\n',conta)
        conta+=1
else:
    print('valore non acconsentito')