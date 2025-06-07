s = input("stringa: ")
i = 0
m = 0
while i < len(s):
    if m < s.count(s[i]):
        i += 1
        m = s.count(s[i])
        break
print(s[m+1])
