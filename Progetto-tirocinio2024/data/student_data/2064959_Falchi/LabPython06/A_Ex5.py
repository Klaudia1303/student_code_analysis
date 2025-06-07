s = input("Inserire una stringa: ")

maxChar = None
maxRec = 0

for i in range(len(s)):
    if s.count(s[i]) >= maxRec:
        maxRec = s.count(s[i])
        maxChar = s[i]

print(maxChar, maxRec)
