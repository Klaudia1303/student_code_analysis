s=input()
c=0
for i in range (0,len(s)//2):
    if (s[i]==s[len(s)-1-i]):
        c+=1
    else:
        break
    if (i==len(s)//2-1):
        c=len(s)
print(c)
