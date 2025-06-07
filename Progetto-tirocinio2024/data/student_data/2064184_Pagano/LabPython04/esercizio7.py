char = ''
charcount = 0

s = input("Inserisci una stringa: ")

for i in range(len(s)):
    count = s.count(s[i])
    if count >= charcount:
        charcount = count
        char = s[i]

print(char)
