s = input("Inserire una stringa: ")
M = 0
i = 0
while i < len(s):
    if s.count(s[i]) >= M:
        M = s.count(s[i])
        pos = i
    i += 1
print(s[pos])
