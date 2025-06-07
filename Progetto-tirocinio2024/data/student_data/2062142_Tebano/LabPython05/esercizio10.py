finish=False
k=1
while finish==False:
    n=int(input('lato='))
    if n%2!=0:
        for i in range (1,n+1):
            if i==n or i==1:
                print(n*'*')
            elif i<=n//2:
                print('*'+' '*(i-2)+'*'+' '*(n-(2*i))+'*'+(' '*(i-2))+'*')
            elif i==n//2+1:
                print('*'+' '*(i-2)+'*'+' '*(i-2)+'*')
            elif i>n//2+1:
                print('*'+' '*(n-1-i)+'*'+' '*(k)+'*'+(' '*(n-1-i)+'*'))
                k=k+2
    elif n%2==0:
        k=0
        for i in range (1,n+1):
            if i==n or i==1:
                print(n*'*')
            elif i<=n//2:
                print('*'+' '*(i-2)+'*'+' '*(n-(2*i))+'*'+(' '*(i-2))+'*')
            
            elif i>n//2:
                print('*'+' '*(n-1-i)+'*'+' '*(k)+'*'+(' '*(n-1-i)+'*'))
                k=k+2            
                      
                
            
