n=int(input('inserire un  numero intero: '))

i=2
while n>2:
    if n%2==0:
        print(n)
        i=n+2
        n=n-1
    elif n%2!=0:
        print(n-1)
        i=n+1
        n=n-2
