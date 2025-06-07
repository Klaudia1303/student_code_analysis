n=int(input())
m=int(input())
i=1
d=0
import math
if (n<0 and m>0)or(n>0 and m<0):
    while i<=abs(m):
        d=d+abs(n)
        i=i+1
    print('-',d)
else:
    while i<m:
        d=d+n
        i=i+1
    print(d)    
        
        

