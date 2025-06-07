s = input("Inserisci una stringa: ")

level = 0

for i in range(len(s)):
    if s[i] == s[-i-1]:
        level += 1
    else:
        break

print(level)
