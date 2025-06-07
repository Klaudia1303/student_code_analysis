n=int(input("inserisci n: "))
m=int(input("inserisci n: "))
i=0
s=0
if m>0:
    while i<m:
        s=s+n
        i=i+1
elif m<0:
    while m<i:
        s=s-n
        i=i-1
    
print(s)
    
