s= str(input())
for c in range(len(s)):
    if s[c]==s[c::-1]:
        t=s.rfind(s[c::-1])
        c=c
        print(t-c)