n1=int(input('inserire un intero   '))
n2=int(input('inserire un intero   '))
n3=int(input('inserire un intero   '))
M=max(n1,n2,n3)
m=min(n1,n2,n3)
if M>n1>m:
    print(M,n1,m)
elif M>n2>m:
    print(M,n2,m)
else:
    print(M,n3,m)

    
