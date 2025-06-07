s = input("Inserire una stringa: ")

for i in range(len(s)):
    if s.find(s[i]) != s.rfind(s[i]):
        print(True)
        exit()

print(False)