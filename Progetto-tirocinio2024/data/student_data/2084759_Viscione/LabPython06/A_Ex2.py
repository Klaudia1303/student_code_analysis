s=input("immetti stringa: ")
p=0
for i in range(len(s)):
    if s[i]==s[-(i+1)]:
        p=p+1
    else:
        break
print(p)
