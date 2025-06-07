n=int(input('insersisci intervallo '))
while n>1:
    divisore=2
    nDivisori=0
    while divisore<=n/2 and nDivisori==0:
        if n%divisore==0:
            nDivisori+=1
        divisore+=1
    if nDivisori==0:
        print(n)
    n-=1
