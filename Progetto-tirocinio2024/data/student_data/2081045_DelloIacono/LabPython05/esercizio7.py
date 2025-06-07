s = input("Inserire una stringa: ")
check = False
for i in range(len(s)):
    if(s.count(s[i])>1):
        check = True
print(check)
