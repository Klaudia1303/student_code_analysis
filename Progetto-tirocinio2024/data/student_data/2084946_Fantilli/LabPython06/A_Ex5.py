s=input()
for i in range(len(s)):
    for j in range(i+1,len(s)):
        if s.count(s[i])>s.count(s[j]):
            for k in range(s.find(s[i]),s.find(s[i])+s.count(s[i])):
                if s[k]==s[k+1]:
                    r=s[k]
        elif s.count(s[j])>s.count(s[i]):
            for k in range(s.find(s[j]),s.find(s[j])+s.count(s[j])):
                if s[k]==s[k+1]:
                    r=s[k]
print(r, s.count(r))
