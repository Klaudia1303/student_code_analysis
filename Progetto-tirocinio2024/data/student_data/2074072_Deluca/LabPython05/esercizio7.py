s=input()
corretto=False
for i in range(0,len(s)):
    if s.count(s[i])>1:
        corretto=True
print(corretto)
