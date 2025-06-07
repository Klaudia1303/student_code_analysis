s=str(input())
t=str(input())
w=''
for i in range(len(s)):
    if s[i] not in t:
        w=w+s[i]
print(w)        
