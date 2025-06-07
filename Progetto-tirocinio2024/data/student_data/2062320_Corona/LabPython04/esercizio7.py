s=input()
i=0
max=s.count(s[i])
maxc=s[i]
while i<len(s):
    if s.count(s[i])>=max:
        max=s.count(s[i])
        maxc=s[i]
    i+=1
print(maxc)