n=int(input())

i=1
a=0
b=1
c=0
while i<=n:
    a=b
    b=c
    c=a+b
    print(c)
    i=i+1
    
