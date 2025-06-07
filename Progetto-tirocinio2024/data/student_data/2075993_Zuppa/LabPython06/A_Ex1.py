n1=int(input('inserire un numero intero maggiore a 0   '))
while n1<=0:
    n1=int(input('inserire un numero intero maggiore a 0   '))
n2=int(input('inserire un numero intero maggiore a 0   '))
while n2<=0:
    n2=int(input('inserire un numero intero maggiore a 0   '))
for i in range(n1,1,-1):
    if n1%i==0 and not n2%i==0:
        print(i)
