s=input('Inserire una stringa:')
dis=0
for i in range(len(s)):
    if dis<s.rfind(s[i])-i:
        dis=s.rfind(s[i])-i
print(dis)

   

