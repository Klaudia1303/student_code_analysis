
s=input("Inserire stringa:\t")
liv=0

for i in range(len(s)):
    if s[i]==s[-i-1]:
        liv=liv+1

    if s[i]!=s[-i-1]:
        break
print(liv)
