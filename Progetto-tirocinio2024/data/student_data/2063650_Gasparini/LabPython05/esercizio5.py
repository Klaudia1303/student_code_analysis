s = input("Stringa: ")
n = int(input("Distanza: "))

presente = False
for i in range(len(s) - n):
    if s[i] == s[i + n]:
        presente = True
        break
print(presente)
