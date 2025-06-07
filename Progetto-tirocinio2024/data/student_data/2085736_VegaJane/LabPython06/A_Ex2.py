s = input("Inserire una stringa: ")
lvl = 0
for i in range(len(s)):
    if s[i]==s[len(s)-i-1]:
        lvl += 1
    else:
        break
print(lvl)
