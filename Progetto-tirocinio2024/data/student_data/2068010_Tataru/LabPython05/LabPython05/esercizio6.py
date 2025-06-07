s=input()
max=0
for i in range(len(s)):
    if s.rfind(s[i])-i>max:
        max=s.rfind(s[i])-i
print(max)