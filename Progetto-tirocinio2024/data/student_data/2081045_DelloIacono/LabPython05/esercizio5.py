s = input("Inserire una stringa: ")
n = int(input("Inserire un numero: "))
check = False
for i in range(len(s)):
    if(s.rfind(s[i]) - s.find(s[i]) == n):
        check = True
print(check)
