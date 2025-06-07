s=input('stringa=')
s1=s
j=False
for i in range(len(s)-1):
    if s[i+1:].find(s1[i])>0:
        j=True
print(j)
