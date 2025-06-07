n=input()
i=0
while n!='*':
    n=int(n)
    if n<=0:
        i=i+n
    n=input()
print(i)    
