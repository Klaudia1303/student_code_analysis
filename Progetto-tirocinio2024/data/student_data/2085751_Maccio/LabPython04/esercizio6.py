n1=int(input("inserire intero: "))
n2=int(input("inserire intero 2: "))
k=0
s=0
if n1==0 or n2==0:
    s=0
elif n1>0 and n2>0:
    while abs(n2)>k:
        s=n1+s
        k+=1
elif n1>0 and n2<0:
    while abs(n2)>k:
        s=(n1+s)
        k+=1
    s=-s
elif n2>0 and n1<0:
    while abs(n2)>k:
        s=(n1+s)
        k+=1
else:
    while abs(n2)>k:
        s=n1+s
        k+=1
    s=-s
print(s)
