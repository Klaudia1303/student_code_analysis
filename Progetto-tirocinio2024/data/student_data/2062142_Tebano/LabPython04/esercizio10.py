a=str(input())
b=str(input())
c=str(input())
while (len(a)==len(b) and len(c)==len(a)+len(b))== False:
    a=b
    b=c
    c=str(input())
print(a,b,c)    
    
