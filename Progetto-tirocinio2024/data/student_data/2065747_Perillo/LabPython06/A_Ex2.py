s=input()
n=0
while n<len(s):
    if s[n]==s[-n-1]:
        n+=1
    else:
        break
print(n)
