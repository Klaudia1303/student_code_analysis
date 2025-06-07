s=input('stringa: ')
dis=0
for i in range(len(s)):
    if s.rfind(s[i])-s.find(s[i])>dis:
        dis=s.rfind(s[i])-s.find(s[i])
print(dis)
