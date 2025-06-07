i=1
fatt=1
n=int(input('inserire un numero intero maggiore o uguale a 0: '))
if n==0 or n==1:
    print(1)
else:
    while i<=n:
        fatt*=i
        i+=1
print(fatt)
