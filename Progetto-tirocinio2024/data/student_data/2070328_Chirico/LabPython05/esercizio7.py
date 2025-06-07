s = input('stringa = ')
ripetizioni = False

for i in range(len(s)):
    if s.rfind(s[i]) != s.find(s[i]):
        ripetizioni = True

print(ripetizioni)
