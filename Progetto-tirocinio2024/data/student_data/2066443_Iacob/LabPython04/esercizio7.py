s = str(input('Insert word here: '))
i = 0
n = 0
while i<len(s):
    if s.count(s[i])>=n:
        n = s.count(s[i])
        m = i
    i = i+1
print(s[m])
