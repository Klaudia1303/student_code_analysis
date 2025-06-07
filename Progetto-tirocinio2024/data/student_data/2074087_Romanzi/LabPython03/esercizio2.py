c=True
while c:
    s=int(input('Intero maggiore di 0 '))
    if s<=0:
        print('Numero non valido ')
    else:
        c=False
k=1
while s>=k:
    if s%k==0:
        print(str(k))
    k=k+1
