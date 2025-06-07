s = input("Stringa: ")

l = 0
for i in range(len(s)):
    if s[i] != s[-(i+1)]:
        break
    l += 1
print(l)
