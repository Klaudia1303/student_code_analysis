s = input("Inserire una stringa: ")
m = 0
for i in range(len(s)):
    for j in range(i+1,len(s)):
        if s[i]==s[j] and j-i > m:
            m = j-i
print(m)
