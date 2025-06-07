s=input('inserire stringa')
n=int(input('inserire numero intero'))
x=False
for i in range(len(s)):
    if n+1<len(s):
        if s[i]==s[n+1]:
            x=True
print(x)
