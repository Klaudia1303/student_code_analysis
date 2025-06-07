s = input('Inserisci stringa: ')
twice = False

for i in range(len(s)):
    if s.find(s[i]) != s.rfind(s[i]):
        twice = True
print(twice)
