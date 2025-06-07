n=int(input())
i=n-1
somma=n
if n==0 or n==1:
    print(1)
else:
    while i>0:
        somma*=i
        i-=1
    print(somma)