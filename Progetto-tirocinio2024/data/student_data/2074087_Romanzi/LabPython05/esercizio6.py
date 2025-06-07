s=str(input('Stringa '))
n=0
k=0
while n<len(s):
    for i in range(len(s)):
        if s[n]==s[i]:
            if i-n>=k:
                k=i-n
    n=n+1
print(k)
