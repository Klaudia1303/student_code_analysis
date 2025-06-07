
c=input("carattere")
t=True
while t==True:
    C=0
    i=0
    s=input("stringa")
    while i<len(s):
        if s[i]==c:
            C+=1
        if i+1==len(s):
        
            if C>2:
                t=False
        i+=1
        
print(C)
