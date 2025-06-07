n=int(input("inserisci un numero maggiore di 0"))
i=1
k=1
print(1)
while i<=n and k<=n:
    i=i+k
    print(i)
    k=i+k
    if k<=n:
        print(k)
