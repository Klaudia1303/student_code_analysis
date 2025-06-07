s=input('inserire una stringa   ')
c=False
for i in range(len(s)):
    if s.count(s[i])>1:
        c=True
print(c)
