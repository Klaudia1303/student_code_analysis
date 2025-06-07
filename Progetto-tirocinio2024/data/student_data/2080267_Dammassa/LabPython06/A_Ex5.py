s = input("stringa: ")
m = 0
for i in range(len(s)):
    if m <= s.count(s[i]):
        m = s.count(s[i])
        k = s[i]

print(k,m)
