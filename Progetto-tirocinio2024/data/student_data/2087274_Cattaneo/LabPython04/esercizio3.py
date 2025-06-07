n=input('n=')
s=0
while n!='*':
    if int(n)<0:
        s=s+int(n)
    n=input('n=')
print(s)
