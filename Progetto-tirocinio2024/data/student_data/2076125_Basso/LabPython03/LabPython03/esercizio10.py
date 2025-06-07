
N=int(input("Inserisci intero maggiore di 1:\t"))
a=1
b=0

n=1

while n <= N:
    while a<= n:
        if n%a==0:
            b=b+1
        a=a+1
    if b==2:
        print(n)
    n=n+1
    b=0
    a=1
