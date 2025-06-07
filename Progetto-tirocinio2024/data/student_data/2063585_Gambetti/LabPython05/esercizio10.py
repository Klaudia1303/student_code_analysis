n=int(input('inserisci un lato dispari e maggiore o uguale a tre: '))
j=0
x=n-4
if n%2!=0 and n!=2:
    s=((n-1)//2)+1
    for i in range(1,2):
        print('*'*n)
    for i in range (2,s):
        spazio=' '*j+'*'+' '*x+'*'+' '*j
        j+=1
        x-=2
        print('*'+spazio+'*')
    for i in range(s,s+1):
        y=(n-3)//2
        print('*'+' '*y+'*'+' '*y+'*')
    for i in range(s+1,n):
        spazio=' '*(j-1)+'*'+' '*(x+2)+'*'+' '*(j-1)
        j-=1
        x+=2
        print('*'+spazio+'*')
    for i in range(n,n+1):
        print('*'*n)
elif n%2==0 and n!=2:
    s=(n//2)-1
    for i in range(1,2):
        print('*'*n)
    for i in range(2,s+1):
        spazio=' '*j+'*'+' '*x+'*'+' '*j
        j+=1
        x-=2
        print('*'+spazio+'*')
    for i in range(s+1,s+3):
        y=(n-4)//2
        print('*'+' '*y+'*'+'*'+' '*y+'*')
    for i in range(s+3,n):
        spazio=' '*(j-1)+'*'+' '*(x+2)+'*'+' '*(j-1)
        j-=1
        x+=2
        print('*'+spazio+'*')
    for i in range(n,n+1):
        print('*'*n)
elif n==2:
    for i in range(1,3):
        print('*'*2)
    
        
        
    
