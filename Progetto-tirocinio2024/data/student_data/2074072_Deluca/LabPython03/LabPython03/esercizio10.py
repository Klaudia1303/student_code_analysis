N=int(input("inserisci un numero positivo"))
n=2
while n<=N:
    k=2
    while  k<n:
          if n%k == 0:
              k=n
          k+=1
    if k==n:
        print(n)
    n+=1

