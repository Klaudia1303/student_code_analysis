s=input('inserire stringa: ')
c=0
for a in range(len(s)):
    if s.rfind(s[a])-s.find(s[a])>c:
        c=s.rfind(s[a])-s.find(s[a])
print(c)
            
