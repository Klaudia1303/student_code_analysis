s=str(input('inserire stringa: '))
counter=False
for i in range(len(s)):
    if s.count(s[i])>1:
        counter=True
print(counter)
