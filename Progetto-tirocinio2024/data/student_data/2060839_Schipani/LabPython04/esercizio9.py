n=int(input('inserisci un numero maggiore di 0 '))
print(1)
i=0
k=1
while i<=n and k<=n:
    i=i+k
    print(i)
    k=i+k
    if k<=n:
        print(k)
