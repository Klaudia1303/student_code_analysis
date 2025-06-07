s=input("Inserire una stringa: ")
o=1
c=s[len(s)-1]
k=1
for i in range(1,len(s)):
    if s[i]==s[i-1]:
        k+=1
        if k>=o:
            o=k
            c=s[i]
    else:
        k=1
print(c, o)