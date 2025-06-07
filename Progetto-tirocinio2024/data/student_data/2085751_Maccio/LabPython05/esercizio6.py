s=input("Inserire una stringa:  ")
k=0
for i in range(len(s)):
    if (s.rfind(s[i])-s.find(s[i]))>k:
        k=s.rfind(s[i])-s.find(s[i])
print(k)
