s = input('Inserisci una stringa: ')
k = 0
for i in range(len(s)):
    for j in range(i+1, len(s)):
        if s[i]==s[j] and j-i > k:
            k = j-i
print(k)
