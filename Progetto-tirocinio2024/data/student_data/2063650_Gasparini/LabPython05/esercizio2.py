s = input("Stringa: ")
n = int(input("Numero di ripetizioni: "))

r = ""
for i in range(len(s)):
    r += s[i] * n
print(r)
