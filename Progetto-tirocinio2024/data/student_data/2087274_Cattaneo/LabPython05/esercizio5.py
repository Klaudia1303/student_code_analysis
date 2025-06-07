s=input('stringa=')
n=int(input('n='))
s1=s
j=False
for i in range(len(s)-1):
    if s[i+1:].find(s1[i])==(n-1):
        j=True
print(j)
