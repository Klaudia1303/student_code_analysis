s=input("Inserisci stringa: ")
check=False
for i in range(len(s)):
    if s.count(s[i])>1:
        check=True
        break
print(check)
