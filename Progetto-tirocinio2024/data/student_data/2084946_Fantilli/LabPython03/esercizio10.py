n = input()
n = int(n)
i = 2
while n%i==0:
    n-=1
while i<=n and n//i!=n/i:
    i+=1
    if i==n:
        print(n)
        n-=1
    else:
        n-=1
