s=input('stringa=')
s1=s
j=0
for i in range(len(s)-1):
    if s[i+1:].rfind(s1[i])>j:
        j=s[i+1:].rfind(s1[i])+1
print(j)
