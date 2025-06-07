s = input("Inserisci una stringa: ")

success = False

for i in range(len(s)):
    if s.rfind(s[i]) != i:
        success = True
        break

print(success)
