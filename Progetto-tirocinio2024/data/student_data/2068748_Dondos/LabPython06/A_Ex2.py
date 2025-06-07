s = input('inserisci una stringa: ')
palindromicita = 0

for i in range(len(s)):
    if s[i] == s[len(s)-1-i]:
        palindromicita += 1
    else:
        break
print(palindromicita)
