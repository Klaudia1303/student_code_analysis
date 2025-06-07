n=int(input('inserire un intero n>0'))
i=0
a=0
b=1
while i<n and n>0:
    somma=a
    a=b
    b=somma+b
    print(a)
    i+=1
