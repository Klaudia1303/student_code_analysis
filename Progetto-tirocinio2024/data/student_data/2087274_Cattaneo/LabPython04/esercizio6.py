n=int(input('n='))
m=int(input('m='))
i=0
s=0
if m==0:
    s=0
if m>0:
    while i<m:
        s=s+n
        i+=1
if m<0:
    while i>m:
        s=s-n
        i-=1
print(s)
