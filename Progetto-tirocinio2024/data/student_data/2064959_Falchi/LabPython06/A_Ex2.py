s = input("Inserire stringa: ")

level = 0

for i in range(0, len(s)):
    if s[i] == s[-i-1]:
        level += 1
    else:
        break
    #print(s[i], s[-i-1])

if level == 0:
    print("La stringa non è palindroma")
else:
    print("La stringa è palindroma (Livello", str(level) + ")")
