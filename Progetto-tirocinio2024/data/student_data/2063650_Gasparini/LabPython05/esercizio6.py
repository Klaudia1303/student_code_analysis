s = input("Stringa: ")

max = 0
for i in range(len(s) - 1):
    c = s[i]
    j = s.rfind(c)
    if j - i > max:
        max = j - i
print(max)
