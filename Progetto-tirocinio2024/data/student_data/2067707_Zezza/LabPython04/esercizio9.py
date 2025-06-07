n=int(input('inserisci intero: '))
i=1
k=1
print(1)
while i<=n and k<=n:
    i=i+k
    print(i)
    k=i+k
    if k<=n:
        print(k)
