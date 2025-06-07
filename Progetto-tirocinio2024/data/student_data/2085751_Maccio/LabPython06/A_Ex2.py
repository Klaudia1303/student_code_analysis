s=input("Inserire una stringa:  ")
g=0
r=True
l=len(s)-1
for i in range(len(s)):
    if s[i]==s[l]:
        g+=1
        l-=1
    else:
        break
print(g)
