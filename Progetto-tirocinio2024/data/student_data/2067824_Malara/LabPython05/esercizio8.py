n=int(input('inserire intero dispari >= a 3: '))
i=1
while i<=n:
    spazio=' '*int((n-i)/2)
    print(spazio,'*'*i)
    i+=2
