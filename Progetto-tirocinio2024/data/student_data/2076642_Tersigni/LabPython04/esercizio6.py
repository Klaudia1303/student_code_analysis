n=int(input("inserisci un intero"))
m=int(input("inserisci un intero"))
k=n
if m==0 or n==0:
    print(0)
else:
    if m>0:
        while m!=1:
            n=n+k
            m=m-1
        print(n)
    else:
        while m!=-1:
            n=n+k
            n=m+1
        print(-n)
