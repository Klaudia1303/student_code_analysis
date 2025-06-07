s = input("Inserire una stringa:")
i = 0
j = len(s)-1
l = 0

while i <= len(s)-1:
    if s[i] == s[j]:
        i += 1
        j -= 1
        l += 1
    else:
        break
print(l)
