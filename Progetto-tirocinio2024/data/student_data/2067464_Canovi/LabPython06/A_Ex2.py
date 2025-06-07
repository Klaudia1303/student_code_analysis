s = input("inserisci una stringa: ")
s1 = s[::-1]
palindrom = 0

for i in range(len(s)):
    if s[i] == s1[i]:
        palindrom = palindrom + 1
    else:   break

print(palindrom)
