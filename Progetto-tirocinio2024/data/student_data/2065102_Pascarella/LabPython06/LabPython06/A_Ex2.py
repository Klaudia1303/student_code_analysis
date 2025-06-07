s=input()
x=0
for i in range (len(s)):
    if s[i]==s[-i-1]:
        x=i+1
    else:
        break
print(x)
