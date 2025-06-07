s = input('Inserisci una stringa: ')

ch = 0
m = 0
i = 0
while i < len(s):
    c = s.count(s[i])
    if (c >= m):
        m = c
        ch = s[i]
    i += 1
print(ch)
