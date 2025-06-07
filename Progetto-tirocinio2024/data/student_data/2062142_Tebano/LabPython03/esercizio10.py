n=int(input())
i=3
p=2
if n==2:
    print('2')
else:
    while i<=n:
        while p<i:
            if i%p==0:
                p=2*i
            else:
                p=p+1
        if p==i:
            print(i)         
        p=2
        i=i+1
    
    
