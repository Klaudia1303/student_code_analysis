s = input("Inserisci una stringa: ")

max = 0

for i in range(len(s)):
    r = s.rfind(s[i])
    if r not in [-1, i] and r-i > max:
        max = r-i

print(max)
