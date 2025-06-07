n1=20
n2=1
n=1
for i in range(1000):
    n1+=20
    n2=n2+(n+1)
    n+=1
    if n1==n2:
        break
print(n)
