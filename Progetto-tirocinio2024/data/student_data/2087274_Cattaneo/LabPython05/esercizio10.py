n=int(input('n='))
for i in range(n):
    if i==0 or i==n-1:
        print('*'*n)
    elif n%2!=0 and i==n//2:
        print('*'+' '*(n//2-1)+'*'+(n//2-1)*' '+'*')
    elif i<n//2:
        print('*'+' '*(i-1)+'*'+' '*(n-2*(i+1))+'*'+' '*(i-1)+'*')
              #tot=n-->2+2+
    else:
        print('*'+' '*(n-i-2)+'*'+' '*(n-2*(n-i))+'*'+' '*(n-i-2)+'*')
