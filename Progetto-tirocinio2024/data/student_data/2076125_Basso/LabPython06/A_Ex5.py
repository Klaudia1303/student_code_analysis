
s=input("Inserire stringa alfanumerica:\t")
c=1
m=1

for i in range(len(s)-1,-1,-1):
    if s[i]==s[i-1]:
        c=c+1
    else:
        if m<c:
            m=c
            c=1
            l=s[i]



    
print(l,m)
