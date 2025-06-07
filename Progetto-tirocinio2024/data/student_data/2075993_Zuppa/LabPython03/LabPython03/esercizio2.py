n=int(input('inserire un intero maggiore a zero   '))
while n<1:
    n=int(input('reinserire il numero   '))
i=1
while i!=n+1:
    if n%i==0:
        print(i)
    i+=1
