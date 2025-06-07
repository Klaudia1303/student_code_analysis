s = input("inserisci stringa: ")

pal_lvl = 0
for i in range(len(s)):
    if s[i] == s[-i-1]:
        pal_lvl += 1
    else:
        break

print(pal_lvl)