n=int(input())
while n<0:
        n=int(input())
i=0
m=1
if n==0:
    print('n!=1')
else:
    while i<n:
        m=m*(n-i)
        i=i+1
    print(n,'!=',m)    
    
    
