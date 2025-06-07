n=int(input("Inserisci la base del trianglo dispara: "))
k=n/2-0.5
i=1
while i<=n:
    print(" "*int(k)+"*"*i)
    i+=2
    k-=1
