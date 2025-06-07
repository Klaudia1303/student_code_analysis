n=int(input("inserire un numero intero:"))
m=int(input("inserire un numero intero:"))
a=0
s=0
if n>=1 and m>=1:
    while a!=n:
        s+=m
        a+=1
    print(s)
elif n==0 or m==0:
    print(0)
elif n>=1 and m<=-1:
    while a!=n:
        s+=m
        a+=1
    print(s)
elif m>=1 and n<=-1:
    while a!=m:
        s+=n
        a+=1
    print(s)
elif m<=-1 and n<=-1:
    while a!=m:
        s+=n
        a+=1
    print(-s)
