s=input("inserire una stringa: ")
r=0
p=0
for i in range(len(s)):
    r=s.rfind(s[i])-i
    if r>=p:
        p=r
print(p)
