s = input("Inserire una stringa: ")
mas = 0
for i in range(len(s)):
    if(s.rfind(s[i]) - s.find(s[i]) > mas):
        mas = s.rfind(s[i]) - s.find(s[i])
print(mas)
