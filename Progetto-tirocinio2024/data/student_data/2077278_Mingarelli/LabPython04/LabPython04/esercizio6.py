n=int(input('inserisci il primo numero '))
m=int(input('inserisci il secondo numero '))
s=0
if m>0 and n>0:
    while m!=0:
        s=s+n
        m-=1
elif m<0 and n>0:
    while m!=0:
        s=s+n
        m+=1
elif n<0 and m<0:
    while m!=0:
        s=s+n
        m+=1
    s=s*-1
else:
    while m!=0:
        s=s+n
        m-=1
print(s)
    
