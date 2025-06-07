s=input("immetti una stringa: ")
i=0
m=0
c=""
while i<len(s):
    n=s.count(s[i])
    if n>=m:
        m=n
        c=s[i]
    i+=1
print(c)
