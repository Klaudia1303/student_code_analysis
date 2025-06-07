s=input("immetti stringa: ")
m=0
for i in range(len(s)):
    if s.rfind(s[i])-i>=m:
        m=s.rfind(s[i])-i
print(m)
