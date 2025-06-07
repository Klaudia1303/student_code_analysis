s = input('Inserisci una stringa: ')
n = int(input('Inserisci una stringa: '))

found = False
co = ''
for i in range(len(s)):
    if (i > n):
        co = s[i - n]
    if (co == s[i]):
        found = True
print(found)
