s = input("Inserire una stringa:")
n = int(input("Inserire un numero:"))

for x in range(len(s)):
    print(s[x] * n, end = "")
