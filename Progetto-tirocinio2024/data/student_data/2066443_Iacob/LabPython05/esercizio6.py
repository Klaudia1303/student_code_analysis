s = str(input('Insert string: '))
m = 0
for i in range(len(s)):
    d = s.rfind(s[i])-i
    if d>m:
        m = d
print(m)
