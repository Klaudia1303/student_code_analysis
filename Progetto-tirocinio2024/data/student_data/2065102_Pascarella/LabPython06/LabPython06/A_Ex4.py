n=0
n1=0
a=0
for i in range (1,1000):
    n=n+20
    n1=n1+i
    a+=1
    if n1==n or n1>n:
        break
print (a)
