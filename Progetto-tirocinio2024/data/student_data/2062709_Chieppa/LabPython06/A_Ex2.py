s=input('inserire stringa: ')
y=len(s)-1
palindromicità=0
for x in range(0,len(s)):
    if s[x]==s[y]:
        palindromicità=palindromicità+1
    elif s[x]!=s[y]:
        break
    y=y-1
print(palindromicità)
