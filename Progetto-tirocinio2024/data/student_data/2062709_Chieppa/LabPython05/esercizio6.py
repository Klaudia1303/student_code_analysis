s=str(input('inserire stringa: '))
counter=0
for i in range(len(s)):
    if s.rfind(s[i])-s.find(s[i])>counter:
        counter=s.rfind(s[i])-s.find(s[i])
print(counter)
