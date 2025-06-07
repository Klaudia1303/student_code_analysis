n=int(input('inserire un numero intero maggiore di 0    '))
while n==0:
    n=int(input('inserire un numero intero maggiore di 0    '))
n1=1
n2=1
s=2
c=True
print(n1)
print(n2)
while s<n:
    if c:
        n1=s
        print(n1)
        s=n1+n2
    if c:
        n2=s
        print(n2)
        s=n1+n2
