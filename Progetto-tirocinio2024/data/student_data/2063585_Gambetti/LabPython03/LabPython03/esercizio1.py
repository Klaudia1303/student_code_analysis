n=int(input('inserire un intero maggiore di due: '))
if n%2==0:
    print(n)
    while n>2:
        sequenza=n-2
        print(sequenza)
        n=n-2
elif n%2==1:
    n=n-1
    print(n)
    while n>2:
        sequenza=n-2
        print(sequenza)
        n=n-2
