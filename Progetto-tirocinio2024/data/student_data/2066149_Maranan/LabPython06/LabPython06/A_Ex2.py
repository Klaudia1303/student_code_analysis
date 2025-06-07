s = input('Inserisci una stringa: ')
i = 0
for j in range(len(s)):
    if s[j]!=s[-j-1]:
        break
    i += 1
print(i)
        
        
