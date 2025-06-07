n=0
while n<=0:
    n=int(input('Inserire un numero intero maggiore di zero: '))
c=1
while c<=n:
    if n%c==0:
        print(c,'\n')
    c+=1
