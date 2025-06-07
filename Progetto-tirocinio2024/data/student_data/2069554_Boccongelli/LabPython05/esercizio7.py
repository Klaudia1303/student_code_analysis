s = input('Inserisci una stringa: ')

found = False
m = 0
for c in s:
    if (s.find(c) != s.rfind(c)):
        found = True
print(found)
